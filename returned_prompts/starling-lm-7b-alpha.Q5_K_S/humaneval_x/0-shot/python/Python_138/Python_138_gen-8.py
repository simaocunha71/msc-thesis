    from itertools import combinations

    def is_equal_to_sum_even(n):
        if n < 8:
            return False
        for i in range(2, n // 4 + 1):
            for j in combinations(range(i, n + 1, i), 4):
                if sum(j) == n:
                    return True
        return False

#
#     def is_equal_to_sum_even(n):
#         if n < 8:
#             return False
#         for i in range(2, n // 4 + 1):
#             for j in itertools.combinations(range(i, n + 1, i), 4):
#                 if sum(j) == n:
#                     return True
#         return False


def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n < 8:
        return False
    for i in range(2, n // 4 + 1):
        for j in combinations(range(i, n + 1, i), 4):
            if sum(j) == n:
                return True
    return False


def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n < 8:
        return False
    for i in range(2, n // 4 + 1):
        for j in combinations(range(i, n + 1, i), 4):
            if sum(j) == n:
               