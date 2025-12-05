import numpy as np
house_size = float(input("enter the house size: "))
rooms = float(input("enter how many rooms there: "))
x = ([house_size, rooms])
w = np.array([1000,1000])
bias = 1000
prediction = np.dot(x,w)+ bias
print(prediction)