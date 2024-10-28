
def choose_num(x, y):
    if y == 0:
        return 0
    else:
        if y % 2 == 0:
            return y
        else:
            if x % 2 == 0:
                return x
            else:
                if x > y:
                    return -1
                else:
                    return choose_num(x, (y - 1))

#print(choose_num(12, 15))
#print(choose_num(13, 12))



# The first function takes two positive numbers x and y and returns the
# biggest even integer number that is in the range [x, y] inclusive. If 
# there's no such number, then the function should return -1.
# The second function takes two positive numbers x and y and returns the
# biggest even integer number that is in the range [x, y] inclusive. If 
# there's no such number, then the function should return -1.
#
# Here are some examples of the function:
#
# choose_num(12, 15) = 14
# choose_num(13, 12) = -1


# The function works by checking if the first parameter is 0. If it is, 
# it returns 0 as the biggest even number is 0. If the first parameter 
# is not 0, it checks if the second parameter is even. If it is, it returns 
# the second parameter. If the second parameter is not even, it checks if the 
# first parameter is even. If it is, it returns the first parameter. If it is 
# not even, it checks if the first parameter is greater than the second 
# parameter. If it is, it returns -1. If it is not, it calls itself with 
# the same parameters but the second parameter is decreased by 1.



```
# Choose Num

# This function takes two positive numbers x and y and returns the biggest even integer number that is in the range [x, y] inclusive. If there’s no such number, then the function should return -1. For example, choose_num