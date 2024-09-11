def consecutive_duplicates(numbers):
    """Remove consecutive duplicates of a given list"""
    result = []
    for i in range(len(numbers)):
        if i == 0 or numbers[i] != numbers[i-1]:
            result.append(numbers[i])
    return result

# Testing
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
print("All tests passed!")




# Time: O(n)
# Space: O(n)
# The reason is that we only add elements to the result list if they are unique or the previous element is not the same as the current one.
# This ensures that we don't add duplicate elements to the result list, which means we don't add any duplicates.
# The space complexity is O(n) because the result list can be considered as space used by the function.

# In the worst case scenario, we might have to add all the elements to the result list, which is why the time complexity is O(n).



# Here are some possible follow-up questions for this problem:

# What if we don't know the length of the input list in advance?
# How can we modify the function to remove consecutive duplicates from an infinite sequence of numbers, such as an infinite stream of numbers from a sensor?
# What if we want to remove consecutive duplicates of a list of dictionaries, tuples, or other data structures that can have duplicates?

# To answer these questions, you can consider implementing the function as a generator or using a circular buffer, among other approaches.
"""

"""


"""

"""

"""


"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""