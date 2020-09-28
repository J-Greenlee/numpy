import numpy as np

integers = np.array([1,2,3])

#print(integers)
#print(type(integers))

integers = np.array([[1,2,3],[4,5,6]])
'''
print(integers.dtype)
print(integers.ndim)
print(integers.shape) #number of dimensions in the array
print(integers.size) #number of elements in the array
print(integers.itemsize)
'''

for row in integers:
    print(row)
    print()

    for col in row:
        print(col,end=' ')
    print()


for i in integers.flat:
    print(i, end=' ')



print(np.zeros(5)) #create an array of 5 zeros (default is float)

print(np.ones(5)) #create an array of 5 ones
print()
print()

array1 = np.ones((2,4),dtype=int) #this creates the array as int and not float
print(array1)
print()

array2 = np.full((3,5),13) #create an array of 3 rows and 5 col of the number 13
print(array2)
print()

print(np.arange(5))
print()

print(np.arange(5,10))
print()

print(np.arange(10,1,-2))
print()

print(np.linspace(0.0,1.0,num=5))
print()

array1 = np.arange(1,21) #changing the previous array to a new one
print(array1)
print()

array2 = array1.reshape(4,5)
print(array2)

'''
array3 = array1.reshape(4,3)    this gives an error
print(array3) '''

array3 = np.arange(1,100001).reshape(4,25000)
print(array3)

array4 = np.arange(1,100001).reshape(100,1000)
print(array4)

numbers = np.arange(1,6)
print(numbers*2) #this is called broadcasting printing the array and multiplying the 
                    #numbers by 2 but not permanently changing it

'''
numbers+=10 #this augments the array and permanently changes it
print(numbers)'''

print(numbers **3)

print(numbers>=13)

numbers2 = np.arange(5,10)
print(numbers2 > numbers)

print(numbers)
print(numbers2)
print(numbers == numbers2)

