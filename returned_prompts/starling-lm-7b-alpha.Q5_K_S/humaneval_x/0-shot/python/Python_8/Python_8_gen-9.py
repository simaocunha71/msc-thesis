    sum_product = 0
    product_product = 1
    for i in numbers:
        sum_product += i
        product_product *= i
    return sum_product, product_product


# Test cases
print(sum_product([]))  # Expected: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected: (10, 24)
print(sum_product([-1, 0, 1, 2, 3]))  # Expected: (3, -6)
print(sum_product([-2, 4]))  # Expected: (2, -8)
print(sum_product([0]))  # Expected: (0, 1)
print(sum_product([-1]))  # Expected: (-1, -1)
print(sum_product([0, 1, 2, 3, 4, 5]))  # Expected: (15, 120)


# More test cases
def test_sum_product():
    assert sum_product([]) == (0, 1)
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([-1, 0, 1, 2, 3]) == (3, -6)
    assert sum_product([-2, 4]) == (2, -8)
    assert sum_product([0]) == (0, 1)
    assert sum_product([-1]) == (-1, -1)
    assert sum_product([0, 1, 2, 3, 4, 5]) == (15, 120)
    print("All test cases passed!")


test_sum_product()


# Recursive Solution
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1
    else:
        first_number = numbers[0]
        remaining_numbers = numbers[1:]
        sum_product_remaining = sum_product(