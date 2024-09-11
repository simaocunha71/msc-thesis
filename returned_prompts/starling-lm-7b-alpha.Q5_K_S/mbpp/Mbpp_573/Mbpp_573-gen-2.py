def unique_product(lst):
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product


# Test Case
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000


# Test Case
assert unique_product([1, 2, 3, 4, 5, 6]) == 120


# Test Case
assert unique_product([0, 0, 0, 0]) == 0


# Test Case
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000


# Test Case
assert unique_product([-1, 0, -2, -3, 1, 2]) == 0


# Test Case
assert unique_product([-100, 0, 0, 0, 0, 0, 0]) == 0


# Test Case
assert unique_product([10, 10, 10, 10, 10, 10, 10, 10]) == 0


# Test Case
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000


# Test Case
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000


# Test Case
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000


# Test Case
assert unique_product([10, 20, 30