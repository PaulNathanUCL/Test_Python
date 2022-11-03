# A file to test bit of Python code

import matplotlib.pylab as plt
import numpy as np



def slow_matvec(matrix, vector):
    assert matrix.shape[1] == vector.shape[0]
    result = []
    for r in range(matrix.shape[0]):
        value = 0
        for c in range(matrix.shape[1]):
            value += matrix[r, c] * vector[c]
        result.append(value)
    return np.array(result)


def fast_matvec(matrix, vector):
    assert matrix.shape[1] == vector.shape[0]
    result = []
    for r in range(matrix.shape[0]):
        value = 0
        slice = matrix[r:r+1,:]
     #   print(slice)
        value = np.dot(slice,vector)
        result.append(value)
    return np.array(result).transpose()


# Example of using this function
matrix = np.random.rand(3, 3)
vector = np.random.rand(3)
print(slow_matvec(matrix,vector))
slow=slow_matvec(matrix,vector)
print(type(slow))

print(fast_matvec(matrix, vector))
fast=fast_matvec(matrix, vector)
print(type(fast))


print(matrix @ vector)
matmult = matrix @ vector
print(matmult)

assert np.allclose(matmult,fast)

from timeit import timeit

n_values=[2, 10, 50, 100, 500]
mult_types=[0,1]
slow_matvec_times=[]
fast_matvec_times=[]

for mult_type in mult_types:
    print(mult_type)
    if mult_type == 0:
        for n_value in n_values:
            def function_to_be_timed():
                matrix = np.random.rand(n_value, n_value)
                vector = np.random.rand(n_value)
                #print(slow_matvec(matrix,vector))
                slow_matvec(matrix,vector)
                return
            t= timeit(function_to_be_timed, number =100)
            print("Time taken was," , t, " seconds for scenario", mult_types,"and n=",n_value)
            slow_matvec_times.append(t)
    else:
        for n_value in n_values:
            def function_to_be_timed():
                matrix = np.random.rand(n_value, n_value)
                vector = np.random.rand(n_value)
                #print(fast_matvec(matrix,vector))
                fast_matvec(matrix,vector)
                return
            t= timeit(function_to_be_timed, number =100)
            print("Time taken was," , t, " seconds for scenario", mult_types,"and n=",n_value)
            fast_matvec_times.append(t)

print("slow_matvec",slow_matvec_times)
print("fast_matvec",fast_matvec_times)



import matplotlib.pylab as plt
import numpy as np

x = n_values
y0 = slow_matvec_times
y1 = fast_matvec_times


plt.plot(x, y0, "ro-")
plt.plot(x, y1, "g^-")
plt.xscale("log")
plt.yscale("log")
plt.axis("equal")


plt.xlabel("Size of matrix")
plt.ylabel("Time in Seconds")
plt.legend(["$slow matvec$", "$fast matvec$"])

plt.show()

np.save("slow_matvec_results.npy", slow_matvec_times)

data = np.load("slow_matvec_results.npy")

print(data)


 




