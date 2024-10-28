
def add(lst):
    res = 0
    for i, val in enumerate(lst):
        if i % 2 == 1 and val % 2 == 0:
            res += val
    return res

# Tests
print(add([4, 2, 6, 7]))  # 2
print(add([2, 3, 4, 5, 6]))  # 6
print(add([7, 8, 9, 10, 11]))  # 18

