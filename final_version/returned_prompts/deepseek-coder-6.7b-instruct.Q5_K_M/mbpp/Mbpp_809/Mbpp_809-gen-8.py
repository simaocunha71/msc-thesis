def check_smaller(t1, t2):
    return all(x < y for x, y in zip(t1, t2))

print(check_smaller((1, 2, 3), (2, 3, 4)))  # False

"""
