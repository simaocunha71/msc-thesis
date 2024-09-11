"""
def extract_singly(lst):
    new_list = []
    for i in lst:
        for j in i:
            new_list.append(j)
    return new_list

assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""

def extract_singly(lst):
    return [item for sublist in lst for item in sublist]

assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])

# Explanation:
# The function extract_singly takes a list of lists as an input. It then uses a list comprehension to iterate through each sublist in the input list, and for each sublist, it iterates through each item in the sublist. The items are appended to a new list, new_list. Finally, the function returns the new_list, which is a single set of numbers. The assert statement tests whether the function correctly flattens the list of lists into a single set of numbers, and asserts that the set of the result of the function is equal to the set of the expected output.

# Time Complexity: O(n), where n is the total number of elements in the list of lists. This is because the function iterates through each element in the list of lists once.

# Space Complexity: O(n), where n is the total number of elements in the list of lists. This is because the function creates a new list to store the flattened elements.

# Stability: The function is stable because it maintains the relative order of the elements in the original list of lists.

# Scalability: The function is scalable because it can handle a large number of elements in the list of lists without running out of memory, as long as the memory complexity is within the system's limits.

# Reliability: The function is reliable because it correctly flattens the list of lists into a single set of numbers, as tested by the assert statement.

# Test