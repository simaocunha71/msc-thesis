def big_sum(numbers):
    """Returns the sum of the smallest and largest element of a given array."""
    return max(numbers) + min(numbers)


# Testing the function
assert big_sum([1, 2, 3]) == 4
print("All test cases passed")



# Testing the function with negative values
assert big_sum([-1, -2, -3]) == -1
print("All test cases passed")


# Testing the function with 0
assert big_sum([0]) == 0
print("All test cases passed")


# Testing the function with more than 3 elements
assert big_sum([1, 2, 3, 4, 5]) == 9
print("All test cases passed")


# Testing the function with more than 3 elements and negative values
assert big_sum([-1, -2, -3, 4, 5]) == 9
print("All test cases passed")


# Testing the function with only negative values
assert big_sum([-1, -2, -3, -4, -5]) == -10
print("All test cases passed")


# Testing the function with more than 3 elements and all equal
assert big_sum([1, 1, 1, 1, 1]) == 4
print("All test cases passed")














"""
Explanation:

The function big_sum takes an array of numbers as input. It uses the max() function to find the largest number in the array and the min() function to find the smallest number in the array. It then adds the largest number and the smallest number together and returns the sum.

The assert statements are used to test the function with different cases. The print statements are used to indicate if all the test cases passed or not.
"""




"""
Explanation:

The function big_sum takes an array of numbers as input. It uses the max() function to find the largest number in the array and the min() function to find the smallest number in the array. It then adds the largest number and the smallest number together and returns the sum.

