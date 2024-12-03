import numpy as np

location_list = np.genfromtxt("input.txt", delimiter='', dtype=int)

first_list = location_list[:, 0]
second_list = location_list[:, 1]

first_list.sort()
second_list.sort()

# part 1

result1 = sum(abs(first_list - second_list))

print(f"part 1 result: {result1}")

first_list = first_list.tolist()
second_list = second_list.tolist()

print(first_list[0:10])

scores = []

for i in range(len(first_list)):
    score = first_list[i] * second_list.count(first_list[i])
    scores.append(score)

print(f"part 2 result: {sum(scores)}")
