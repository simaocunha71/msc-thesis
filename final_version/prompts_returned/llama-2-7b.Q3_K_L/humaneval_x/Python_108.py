
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    n = len(arr)
    res = []
    for num in arr:
        if(num >= 0):
            res.append(-1)
        elif(num < 0 and not is_negative(num)):
            res.append(1)
        else:
            res.append(2)
            
    return sum(res[:-1])

# Returns True if the number is negative, False otherwise
def is_negative(x):
    if(int(str(x)[0]) == -1):  # first digit is negative
        return True
    
    elif(int(str(x)[0] * 8) + int(str(x)[1:])) > 9:  # second digit is positive, but it's too big to be a single digit
        return False 
            
    else:  # number has no negative digits
        return True
```