
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            return i
    return -1

print(choose_num(12, 15))
print(choose_num(13, 12))

# Alternate Solution

def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            return num
    return -1

print(choose_num(12, 15))
print(choose_num(13, 12))

# Alternate Solution

def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) → 14
    choose_num(13, 12) → -1
    """
    return next((i for i in range(y, x - 1, -1) if i % 2 == 0), -1)

print(choose_num(12, 15))
print(choose_num(13, 12))

# Alternate Solution

def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) →