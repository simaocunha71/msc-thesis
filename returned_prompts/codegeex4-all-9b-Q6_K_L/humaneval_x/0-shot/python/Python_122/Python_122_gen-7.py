def add_elements(arr, k):
    return sum(int(x) for x in arr[:k] if len(str(x)) <= 2)

print(add_elements([111,21,3,4000,5,6,7,8,9], 4)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 1)) # 21
print(add_elements([111,21,3,4000,5,6,7,8,9], 9)) # 72
print(add_elements([111,21,3,4000,5,6,7,8,9], 2)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 3)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 5)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 7)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 8)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 9)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 10)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 0)) # 0
print(add_elements([111,21,3,4000,5,6,7,8,9], -1)) # 0
print(add_elements([111,21,3,4000,5,6,7,8,9], 100)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], -100)) # 0