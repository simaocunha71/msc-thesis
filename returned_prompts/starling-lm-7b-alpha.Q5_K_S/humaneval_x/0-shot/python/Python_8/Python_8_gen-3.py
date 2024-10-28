    sum_product = lambda numbers: (sum(numbers), reduce(lambda x, y: x * y, numbers))
    return sum_product(numbers)


# Test Cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
print(sum_product([1, 2, -3, 4]))  # (6, -24)
print(sum_product([10, -5, -2, 3]))  # (8, -300)


def test_sum_product(numbers: List[int]) -> None:
    assert sum_product(numbers) == (sum(numbers), reduce(lambda x, y: x * y, numbers))


test_sum_product([])
test_sum_product([1, 2, 3, 4])
test_sum_product([1, 2, -3, 4])
test_sum_product([10, -5, -2, 3])


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_product = lambda numbers: (sum(numbers), reduce(lambda x, y: x * y, numbers))
    return sum_product(numbers)


# Test Cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
print(sum_product([1, 2, -3, 4]))  # (6, -24)
print(sum_product([10, -5, -2,