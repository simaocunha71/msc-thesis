    return s == s[::-1]


def has_equal_sums(numbers: List[int]) -> bool:
    """ Check if the sum of the first half of the given list of integers is equal to the sum of the second half.

    Example:
        has_equal_sums([1, 2, 3, 4, 5, 6]) ==> False