    def choose_num(x, y):
        if x >= 0 and y >= 0:
            if (y - x) % 2 == 0:
                return max(x, y)
            else:
                if y % 2 == 0:
                    return y
                else:
                    return -1
        else:
            return -1
    return choose_num(x, y)

# Python3 program to find
# maximum even number
# in the range [x, y]

# Function to find maximum even number
# in the range [x, y]
def choose_num(x, y):
    # if both x and y are positive
    if x >= 0 and y >= 0:
        # if difference between y and
        # x is even
        if (y - x) % 2 == 0:
            return max(x, y)
        else:
            # if y is even return y
            if y % 2 == 0:
                return y
            else:
                # else return -1
                return -1
    else:
        # if either x or y is negative
        # return -1
        return -1

# Driver program
x, y = 2, 5
print(choose_num(x, y))



def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x >= 0 and y >= 0:
        if (y - x) % 2 == 0:
            return max(x, y)
        else:
            if y % 2 == 0:
                return y
            else:
                return -1
    else:
        return -1

    return choose_num(x, y)

# Python