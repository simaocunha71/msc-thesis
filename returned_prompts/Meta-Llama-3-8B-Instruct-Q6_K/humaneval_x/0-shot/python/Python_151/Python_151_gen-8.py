def double_the_difference(lst):
    result = 0
    for num in lst:
        if isinstance(num, int) and num > 0:
            result += num ** 2
    return result
    # Write a function that takes a list of numbers as input and returns the sum of squares of the numbers in the list that are odd.
    # The function should ignore numbers that are negative or not integers.
    # If the input list is empty, the function should return 0.
    # For example, the function should return 1 + 9 + 0 + 0 = 10 for the input list [1, 3, 2, 0].  It should return 0 for the input list [-1, -2, 0].
    # It should return 81 for the input list [9, -2].  It should return 0 for the input list [0].

# Testing the function
print(double_the_difference([1, 3, 2, 0]))  # Expected output: 10
print(double_the_difference([-1, -2, 0]))  # Expected output: 0
print(double_the_difference([9, -2]))  # Expected output: 81
print(double_the_difference([0]))  # Expected output: 0
print(double_the_difference([]))  # Expected output: 0
# Testing the function with a list of only negative numbers
print(double_the_difference([-1, -2, -3, -4, -5]))  # Expected output: 0
# Testing the function with a list of only non-integer values
print(double_the_difference([1.5, 2.5, 3.5, 4.5]))  # Expected output: 0
# Testing the function with a list of only zero
print(double_the_difference([0, 0, 0, 0]))  # Expected output: 0
# Testing the function with a list of only one number
print(double_the_difference([5]))  # Expected output: 25
# Testing the function with a list of multiple numbers
print(double_the_difference([1, 3, 5, 7, 9]))  # Expected output: 1 + 9 + 25 + 49 + 81 = 165

# This function works by iterating over each number in the input list.  It checks if the number is an integer and if