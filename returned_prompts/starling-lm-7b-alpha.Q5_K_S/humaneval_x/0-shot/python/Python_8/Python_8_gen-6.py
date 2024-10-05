def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Initialize a variable to store the sum of all the integers in the list
    sum_val = 0

    # Initialize a variable to store the product of all the integers in the list
    product_val = 1

    # Iterate through all the integers in the list
    for i in numbers:
        # Add the current integer to the sum
        sum_val += i

        # Multiply the current integer to the product
        product_val *= i

    # Return a tuple consisting of the sum and the product
    return (sum_val, product_val)

# Test Case 1
result = sum_product([])
print(result)  # Expected Output: (0, 1)

# Test Case 2
result = sum_product([1, 2, 3, 4])
print(result)  # Expected Output: (10, 24)

# Test Case 3
result = sum_product([-1, -2, -3, -4])
print(result)  # Expected Output: (-6, 24)

# Test Case 4
result = sum_product([1, 2, 3, 4, 5])
print(result)  # Expected Output: (15, 120)

# Test Case 5
result = sum_product([0])
print(result)  # Expected Output: (0, 0)

# Test Case 6
result = sum_product([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(result)  # Expected Output: (945, 100000)

# Test Case 7
result = sum_product([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100])
print(result)  # Expected Output: (0, 1)

# Test