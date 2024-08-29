def average_tuple(tup):
    return [sum(x)/len(x) for x in tup]

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

# Alternative solution using list comprehension
def average_tuple(tup):
    return [sum(i)/len(i) for i in tup]

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

# Alternative solution using map and lambda function
def average_tuple(tup):
    return list(map(lambda x: sum(x)/len(x), tup))

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

# Alternative solution using numpy mean function
import numpy as np
def average_tuple(tup):
    return list(np.mean(list(tup), axis=1))

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

# Alternative solution using list and for loop
def average_tuple(tup):
    avg = []
    for i in tup:
        sum = 0
        for j in i:
            sum += j
        avg.append(sum/len(i))
    return avg

print(a