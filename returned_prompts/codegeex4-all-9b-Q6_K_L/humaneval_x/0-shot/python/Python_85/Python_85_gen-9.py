def add(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 0)

print(add([4, 2, 6, 7]))  # 2
print(add([1, 2, 3, 4, 5, 6]))  # 8
print(add([2, 4, 6, 8, 10]))  # 0
print(add([1, 3, 5, 7, 9]))  # 0