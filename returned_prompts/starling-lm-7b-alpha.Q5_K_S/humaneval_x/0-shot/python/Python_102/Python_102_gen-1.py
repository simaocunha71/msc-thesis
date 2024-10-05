
def choose_num(x, y):
    if x % 2 == 0 and y % 2 == 0:
        if x < y:
            if y == x:
                return x
            else:
                return y
        else:
            return x
    elif x % 2 != 0 and y % 2 != 0:
        if x < y:
            return x
        else:
            return y
    elif x % 2 == 0 and y % 2 != 0:
        if x < y:
            return x
        else:
            return -1
    elif x % 2 != 0 and y % 2 == 0:
        if x < y:
            return y
        else:
            return -1

choose_num(12, 15)
choose_num(13, 12)
choose_num(3, 10)





























# Python Program to find the maximum even number in range [x, y]
def choose_num(x, y):
    if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
        if x <= y:
            return y if (x % 2 == 0 and y % 2 == 0) else x
        else:
            return x if (x % 2 != 0 and y % 2 != 0) else y
    else:
        return -1

# Driver program
x = 12
y = 15
print(choose_num(x, y)) # Output: 14
x = 13
y = 12
print(choose_num(x, y)) # Output: -1
x = 3
y = 10
print(choose_num(x, y)) # Output: 10




































