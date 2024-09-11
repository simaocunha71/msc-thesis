def second_smallest(nums):
    sorted_list = sorted(nums)
    return sorted_list[1]

# Test
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
print("Test Passed")




"""
The function works by taking in a list of numbers and then sorting the list in ascending order using the sorted() function. After the list is sorted, the second smallest element is returned using indexing.

The function can be tested using the assert statement to verify that the result of second_smallest([1, 2, -8, -2, 0, -2]) is -2, as expected.

The print statement is used to indicate that the test passed.
"""

"""
To improve the function, it can be optimized to find the second smallest element in a single pass through the list, without the need for sorting. This can be done by keeping track of the current smallest and second smallest elements while iterating through the list.
"""

def second_smallest_optimized(nums):
    smallest = None
    second_smallest = None

    for num in nums:
        if smallest is None or num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or num < second_smallest:
            second_smallest = num

    return second_smallest

# Test
assert second_smallest_optimized([1, 2, -8, -2, 0, -2])==-2
print("Test Passed")

"""
The optimized function works by initializing two variables, smallest and second_smallest, to None. It then iterates through the list of numbers. For each number, it checks if the current smallest is None or if the current number is smaller than the current smallest. If either condition is true, it updates the second_smallest to the current smallest and the smallest to the current number. If the current number is not smaller than the current smallest but is smaller than the second smallest, it updates the second_smallest to the current number.

After iterating through the entire list, the function returns the second smallest element, which is stored in the second_small