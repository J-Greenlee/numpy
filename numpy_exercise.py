import numpy as np
import random

grades = np.random.randint(60,101,12).reshape(3,4)

print(grades)

print("ALl grades: ",grades.mean())

print("Avg by each test: ",grades.mean(axis=0))

print("Avg by each student: ",grades.mean(axis=1))