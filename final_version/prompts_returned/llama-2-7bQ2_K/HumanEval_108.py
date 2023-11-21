
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

    # Count first and last element
    for i in range(-n//2,n-n//2+1):
        if arr[i] > 0:
            continue
        elif arr[i] < 0:
            continue
        else:
            res.append(arr[i])
    
    return res