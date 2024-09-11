def pos_count(lst):
    pos_list = []
    for i in lst:
        if i > 0:
            pos_list.append(i)
    return len(pos_list)

# Test Case:
assert pos_count([1,-2,3,-4]) == 2

# Time Complexity: O(n)
# Space Complexity: O(n)

# Here, n is the length of the list.

"""
This function works by iterating through the input list and appending each positive number to a new list called "pos_list". At the end of the iteration, the function returns the length of "pos_list", which represents the count of positive numbers in the input list.

The time complexity of this function is O(n), as it iterates through the input list once. The space complexity is also O(n), as the function creates a new list with a size equal to the number of positive numbers in the input list.
"""

# Here's an example of how to use the function:

input_list = [1, -2, 3, -4, 5, -6]
positive_count = pos_count(input_list)
print(positive_count)  # Output: 3

# In this example, the function is called with the input list [1, -2, 3, -4, 5, -6]. It correctly identifies the positive numbers in the list (1, 3, and 5) and returns their count, which is 3.

"""
This function can be used to count the number of positive numbers in any given list. It is particularly useful when you want to determine the proportion of positive numbers in a dataset or perform further analysis based on the count of positive numbers.
"""

# Here's another example of how to use the function:

input_list = [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]
positive_count = pos_count(input_list)
print(positive_count)  # Output: 5

# In this example, the function is called with the input list [0, -1, 2, -3, 4