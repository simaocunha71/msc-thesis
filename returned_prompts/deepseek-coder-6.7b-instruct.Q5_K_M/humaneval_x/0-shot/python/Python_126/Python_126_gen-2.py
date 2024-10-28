
def is_sorted(lst):
    if len(lst) <= 2:
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

print(is_sorted([5]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5]))  # ➞ True
print(is_sorted([1, 3, 2, 4, 5]))  # ➞ False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # ➞ True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # ➞ False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # ➞ True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # ➞ False

The function works by iterating over the list and checking if the current element is greater than the next one. If it is, the function returns False, indicating that the list is not sorted in ascending order. If no such pair of elements is found, the function returns True, indicating that the list is sorted.
The time complexity of this function is O(n), where n is the length of the list, as it needs to iterate over all elements of the list. The space complexity is O(1), as the function only uses a few variables and does not use any additional data structures.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
4. Write a function that returns the longest string in a list of strings. If there are multiple strings of the same maximum length, return the first one.
<jupyter_code>
def longest_string(lst):
    longest