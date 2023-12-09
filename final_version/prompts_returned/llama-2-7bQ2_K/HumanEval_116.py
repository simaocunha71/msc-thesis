
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """

    if not isinstance(arr, list):
        raise TypeError("input must be List type")

    # convert input to lowercase and remove non numeric characters from string
    arr_lc = [str(x) for x in arr]
    arr_nums = [x.isnumeric() for x in arr_lc]

    sorted_arr = sorted(arr_nums, key=lambda x: int(x))

    if sorted_arr == arr_lc:
        return sorted_arr
    
    # convert input to binary representation and keep track of ones
    ones = Counter([int('1') for x in range(256)])
    if not isinstance(ones, Counter):
        raise TypeError("input must be Counter type")

    for i in sorted_arr:
        if "1" < int(i):
            continue
        else:
            ones[int("1")] -= 1
            break
        
    # convert the binary representation into decimal and keep track of ones again
    decimals = Counter()
    # reset the count to zero because if input is non-positive integer then we will raise OverflowError
    for one in sorted(ones, reverse=True):
        if "1" < int(one) != False:
            continue
        else:
            decimals[int("0")] += 1

    # convert ones to decimal and