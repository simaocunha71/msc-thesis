    sum_number = 0
    product_number = 1
    for number in numbers:
        sum_number += number
        product_number *= number
    return sum_number, product_number


# Tests
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
print(sum_product([-1, -2, -3, -4]))  # (-10, 24)
print(sum_product([1.0, 2.0, 3.0, 4.0]))  # (10.0, 24.0)
print(sum_product([1, 0, 2, 0]))  # (3, 0)
print(sum_product([0]))  # (0, 1)


# Tests for edge cases
print(sum_product([]))  # (0, 1)
print(sum_product([0]))  # (0, 1)
print(sum_product([1]))  # (1, 1)
print(sum_product([-1]))  # (-1, 1)


# Recursive solution
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1
    else:
        sum_number, product_number = sum_product(numbers[1:])
        return sum_number + numbers[0], product_number * numbers[0]


# Tests for recursive solution
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
print(sum_product([-1, -2, -3, -4]))  # (-10, 24)
print(sum_product([1.0, 2.0, 3.0, 4.0]))  # (10.0, 24.0)
print(sum_product([1, 0, 2, 0]))  # (