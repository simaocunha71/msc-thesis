def filter_oddnumbers(nums):
    """
    Filter odd numbers.

    >>> filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
    True
    """
    result = []
    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result