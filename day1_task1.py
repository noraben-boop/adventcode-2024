import numpy as np

location_list = np.genfromtxt("input.txt", delimiter='', dtype=int)

print(location_list[0:10,:])

first_list = location_list[:, 0]
second_list = location_list[:, 1]

first_list.sort()
second_list.sort()

result = sum(abs(first_list - second_list))

print(result)
