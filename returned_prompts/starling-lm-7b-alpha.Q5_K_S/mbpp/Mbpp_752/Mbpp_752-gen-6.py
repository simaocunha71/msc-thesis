def jacobsthal_num(n):
    """
    Finds the nth jacobsthal number.

    >>> jacobsthal_num(5)
    11
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return 2 * jacobsthal_num(n - 1) + jacobsthal_num(n - 2) + jacobsthal_num(n - 3)

def jacobsthal_num_list(n):
    """
    Finds the first n jacobsthal numbers.

    >>> jacobsthal_num_list(5)
    [0, 1, 1, 3, 5]
    """
    result = [0, 1, 1]
    for i in range(3, n+1):
        result.append(2*result[i-1] + result[i-2] + result[i-3])
    return result[:n+1]

# Testing
print(jacobsthal_num_list(5))


def jacobsthal_num_iter(n):
    """
    Finds the first n jacobsthal numbers using iteration.

    >>> jacobsthal_num_iter(5)
    [0, 1, 1, 3, 5]
    """
    result = [0, 1, 1]
    for i in range(3, n+1):
        result.append(2*result[i-1] + result[i-2] + result[i-3])
    return result[:n+1]

# Testing
print(jacobsthal_num_iter(5))


def jacobsthal_num_rec(n):
    """
    Finds the first n jacobsthal numbers using recursion.

    >>> jacobsthal_num_rec(5)
    [0, 1, 1, 3, 5