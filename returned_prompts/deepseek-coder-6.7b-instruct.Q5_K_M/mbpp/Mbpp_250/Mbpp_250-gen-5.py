
def count_X(tup,ele):
    return tup.count(ele)

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4)) # 0

# If you want to use a for loop
def count_X(tup, ele):
    count = 0
    for i in tup:
        if i == ele:
            count += 1
    return count

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4)) # 0

# If you want to use list comprehension
def count_X(tup, ele):
    return len([i for i in tup if i == ele])

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4)) # 0

# If you want to use a lambda function along with map function
def count_X(tup, ele):
    return sum(map(lambda x: 1 if x == ele else 0, tup))

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4)) # 0

# If you want to use a dictionary and its get method
def count_X(tup, ele):
    dict_count = {i: tup.count(i) for i in tup}
    return dict_count.get(ele, 0)

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4)) # 0

# If you want to use collections library's Counter
from collections import Counter
def count_X(tup, ele):