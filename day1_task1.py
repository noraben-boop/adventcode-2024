import numpy as np

location_list = np.genfromtxt('day1_task1.csv', delimiter=',', dtype=int)

print(location_list[0:10,:])

first_list = location_list[:, 0]
second_list = location_list[:, 1]

first_list[0] = 80784

print(first_list[0])

first_list.sort()
second_list.sort()

result = sum(first_list - second_list)

print(result)



