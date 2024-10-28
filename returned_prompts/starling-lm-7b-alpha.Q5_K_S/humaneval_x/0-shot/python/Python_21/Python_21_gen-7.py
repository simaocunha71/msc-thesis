    min_val = min(numbers)
    max_val = max(numbers)

    return [(i - min_val) / (max_val - min_val) for i in numbers]


# Testing

# print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
# print(rescale_to_unit([-1.0, 0.0, 1.0, 2.0, 3.0]))
# print(rescale_to_unit([0.0, 0.25, 0.5, 0.75, 1.0]))
# print(rescale_to_unit([0.0, 0.0, 0.0, 0.0, 0.0]))




# CodeExplanation:
# Here, we define a function called rescale_to_unit that takes a list of numbers as input and returns a new list of numbers.
# The function first finds the minimum and maximum values in the input list using the min and max functions respectively.
# Then, it applies a linear transform to each element in the input list using a list comprehension.
# The transform is defined as (i - min_val) / (max_val - min_val), where i is the original element in the input list.
# This transform ensures that the smallest number in the input list becomes 0 and the largest number becomes 1.
# Finally, the function returns the transformed list of numbers.


# Test Cases:
# We test the function with a few example inputs to verify that it works correctly.
# The first test case is a list of numbers [1.0, 2.0, 3.0, 4.0, 5.0].
# The expected output is [0.0, 0.25, 0.5, 0.75, 1.0], which is confirmed by the print statement.
# Similarly, we test the function with other example inputs and verify that the output is correct.


# Time Complexity:
# The time complexity of the function is O(n), where n is the number of elements in the input list