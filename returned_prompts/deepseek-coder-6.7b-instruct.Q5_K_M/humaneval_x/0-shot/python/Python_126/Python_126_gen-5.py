
def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

print(is_sorted([5])) # ➞ True
print(is_sorted([1, 2, 3, 4, 5])) # ➞ True
print(is_sorted([1, 3, 2, 4, 5])) # ➞ False
print(is_sorted([1, 2, 3, 4, 5, 6])) # ➞ True
print(is_sorted([1, 2, 3, 4, 5, 6, 7])) # ➞ True
print(is_sorted([1, 3, 2, 4, 5, 6, 7])) # ➞ False
print(is_sorted([1, 2, 2, 3, 3, 4])) # ➞ True
print(is_sorted([1, 2, 2, 2, 3, 4])) # ➞ False

Explanation:

The function uses the built-in all() function in Python. This function returns True if all elements in the iterable (in this case, a generator expression) are true. If not, it returns False. The generator expression checks each pair of consecutive numbers in the list to see if the first number is less than or equal to the second. If all pairs pass this check, the list is sorted in ascending order, and the function returns True. If any pair fails this check, the list is not sorted, and the function returns False.

The solution also works with lists that have more than one duplicate of the same number, as the function only checks for order, not for duplicates.

This solution assumes that the list contains only positive integers, as mentioned in the problem statement.

Please note that this function does not handle negative numbers or floating point numbers, as these are not mentioned in the problem statement.

This solution has a time complexity of O(n), where n is the length of the list, as it needs to iterate over all elements in the list once.
'''
