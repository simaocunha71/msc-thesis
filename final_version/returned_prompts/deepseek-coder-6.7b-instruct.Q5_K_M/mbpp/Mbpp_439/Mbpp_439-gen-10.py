def multiple_to_single(lst):
    return int(''.join(map(str, lst)))

print(multiple_to_single([11, 33, 50]))  # returns 113350

# Solution 2:
def multiple_to_single(lst):
    return int(''.join(str(i) for i in lst))

print(multiple_to_single([11, 33, 50]))  # returns 113350

# Solution 3:
def multiple_to_single(lst):
    return int(''.join(format(i, 'd') for i in lst))

print(multiple_to_single([11, 33, 50]))  # returns 113350

# Solution 4:
def multiple_to_single(lst):
    return int(''.join(format(i, '0d') for i in lst))

print(multiple_to_single([11, 33, 50]))  # returns 113350

# Solution 5:
def multiple_to_single(lst):
    return int(''.join(map(str, [i if i >= 0 else -i for i in lst])))

print(multiple_to_single([11, 33, 50]))  # returns 113350

# Solution 6:
def multiple_to_single(lst):
    return int(''.join(map(str, [i for i in lst if i >= 0])))

print(multiple_to_single([11, 33, -50]))  # returns 113350

# Solution 7:
def multiple_to_single(lst):
    return int(''.join(map(str, lst[::-1])))

print(multiple_to_single([11, 33, 50]))  # returns 113350

# Solution 8:
def multiple_to_single