def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k,
    return the sum of the elements with at most two digits from the first k elements of arr.

    :param arr: List[int] - a non-empty list of integers
    :param k: int - an integer representing the number of elements to consider from the start of the list
    :return: int - the sum of the elements with at most two digits from the first k elements of arr

    >>> add_elements([111,21,3,4000,5,6,7,8,9], 4)
    24
    """
    return sum(num for num in arr[:k] if num < 100)

C:
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k,
    return the sum of the elements with at most two digits from the first k elements of arr.

    :param arr: List[int] - a non-empty list of integers
    :param k: int - an integer representing the number of elements to consider from the start of the list
    :return: int - the sum of the elements with at most two digits from the first k elements of arr

    >>> add_elements([111,21,3,4000,5,6,7,8,9], 4)
    24
    """
    return sum(num for num in arr[:k] if num < 100)

