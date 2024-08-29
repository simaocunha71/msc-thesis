def check_smaller(t1, t2):
    for i, j in zip(t1, t2):
        if i >= j:
            return False
    return True

print(check_smaller((1, 2, 3), (2, 3, 4)))  # False
print(check_smaller((1, 2, 3), (1, 2, 4)))  # False
print(check_smaller((1, 2, 3), (1, 2, 3)))  # False
print(check_smaller((1, 2, 3), (0, 1, 2)))  # True

# Or using list comprehension
def check_smaller(t1, t2):
    return all([i < j for i, j in zip(t1, t2)])

print(check_smaller((1, 2, 3), (2, 3, 4)))  # False
print(check_smaller((1, 2, 3), (1, 2, 4)))  # False
print(check_smaller((1, 2, 3), (1, 2, 3)))  # False
print(check_smaller((1, 2, 3), (0, 1, 2)))  # True

# Or using map function
def check_smaller(t1, t2):
    return all(map(lambda x, y: x < y, t1, t2))

print(check_smaller((1, 2, 3), (2, 3, 4)))  # False
print(check_smaller((1, 2, 3), (1, 2, 4)))  # False
print(check_smaller((1, 2, 3), (1, 2, 3)))  # False
print(check_smaller((1, 2, 3), (0, 1, 2)))  # True

# Or using the built-in all function with a generator expression
def check_smaller(t1, t2):
    return all(x < y for x, y in zip(t1,