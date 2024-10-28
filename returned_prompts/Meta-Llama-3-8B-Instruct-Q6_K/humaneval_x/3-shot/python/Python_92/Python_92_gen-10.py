    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    if x + y == z:
        return True
    if x + z == y:
        return True
    if y + z == x:
        return True
    return False
# another way to do it
def any_int(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    return (x + y == z) or (x + z == y) or (y + z == x)  # use or operator for short circuit evaluation
# or you can use set 
def any_int(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    return set([x, y, z]).count(x + y - z) == 1  # check if any number is equal to the sum of other two and return True if found
# also you can use list comprehension
def any_int(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    return [i + j - k for i, j, k in [(x, y, z), (x, z, y), (y, z, x)]].count(0) == 1  # check if any number is equal to the sum of other two and return True if found
# you can also use zip and map
def any_int(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    return list(map(lambda t: t[0] + t[1] - t[2], zip([x, y, z], [y, z, x], [z, x, y]))).count(0) == 1  # check if any number is equal to the sum of other two and return True if found
# you can also use itertools
def any_int(x, y, z):
    import itertools
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    return list(map(lambda t: t[0] + t[1] - t[