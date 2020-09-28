import numpy as np

grades = np.array([[87,96,70],[100,87,90],
                    [94,77,90],[100,81,82]])
'''
print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())
print(grades.std())
print(grades.var())

print(grades.mean(axis=0))
print(grades.mean(axis=1))
print()
'''
numbers = np.array([1,4,9,16,25,36])
#print(np.sqrt(numbers))
#print()


grades = np.array([[87,96,70],[100,87,90],
                    [94,77,90],[100,81,82]])
'''
print(grades[0,1])
print(grades[1])

print(grades[0:2])
print()

#print(grades[[1,3]])
print()
'''
#print(grades)
#print(grades[:,0]) #this is saying all the rows but only the first column
#print(grades[:1])


#shallow copies via the view command
numbers = np.arange(1,6)
numbers2 = numbers.view()

#print(numbers2)

numbers2[1] /= 10
#print(numebers)

numbers2 = numbers[0:3]
#print(numbers2)

numbers[1] *= 20
#print(numbers2)


#deep copies via the copy command
numbers2 =numbers.copy()

grades = np.array([[87,96,70],[100,87,90]])
#print(grades.reshape(1,6))

#print(grades)

flattened = grades.flatten()
#print(flattened)

raveled = grades.ravel()
#print(raveled)

raveled[5] = 99
#print(grades)

grades2 = grades.T #transposing


grades = np.array([[87,96,70],[100,87,90]])
grades2 = np.array([[94,77,90],[100,81,82]])

h_grades = np.hstack((grades,grades2))
print(h_grades)
print()

v_grades =np.vstack((grades,grades2))
print(v_grades)