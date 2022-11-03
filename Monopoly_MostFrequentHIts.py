#importing libraries
import random
import csv



#declaring variables
turn_counter = 0
total_number_of_turns = 1000000
board_position = 0

#defining board matrix
# 0 - Name on Monopoly Board
# 1 - Family
#       Chance
#       Community Chest
#       Station
#       Utility
#       Tax
#       Property Colour
# 2 - Board position 0 to 39
# 3 - Goto (i.e. does it move you somewhere else) either -1 (nothing) or a board position
# 4 - Landing Counter - How many times have you landed on that square


# Setting Landings to 0 across array
rows, cols = (40, 5)
game_board = [[0 for i in range(cols)] for j in range(rows)]
print(game_board)
print('')

rows, cols = (40, 3)
game_board_numbers = [[0 for i in range(cols)] for j in range(rows)]
print(game_board_numbers)
print('')

# Import Text File with Static Board Data

file_CSV = open("Monopoly_Board.csv", mode='r', encoding='utf-8-sig')
data_CSV = csv.reader(file_CSV)
game_board = list(data_CSV)
print(game_board)
print('')

#Conversion of strings to integers where needed and putting into separate array
row_counter = 0

while row_counter < 40:
    column_counter = 2
    while column_counter <5:
        game_board_numbers[row_counter][column_counter-2]=int(game_board[row_counter][column_counter])
   
        column_counter = column_counter +1
        
    row_counter = row_counter +1

#main game routine
while turn_counter < total_number_of_turns:
    
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    dice_roll = dice_1 + dice_2

# move according to dice roll
    board_position = (board_position + dice_roll) % 40

# if land on Go to Jail
    
    if board_position == 30:
        board_position = 10        


#    print("Dice Roll is ", dice_roll)
#    print("Turn is ", turn_counter)
#    print("Board Position is ", board_position)
    game_board_numbers[board_position][2] = game_board_numbers[board_position][2] + 1
 

    turn_counter +=1


print(game_board_numbers)
print(" ")

#Sort the output

def sorter(item):
    # Want to sort on the Landings Count but also return the position reference
    landings = item[2]
    position_ref = item[0]
    return (landings, position_ref)


sorted_list = sorted(game_board_numbers, key=sorter, reverse=True)
print("Monopoly Squares in order:")
print(sorted_list)

# Write the output to a csv file
header = ['Number of Landings', 'Position Ref']

with open('Monopoly_Landings_Output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(sorted_list)


