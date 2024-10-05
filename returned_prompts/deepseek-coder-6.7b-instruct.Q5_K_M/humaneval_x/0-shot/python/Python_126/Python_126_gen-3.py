
def is_sorted(lst):
    if len(lst) == 1:
        return True
    else:
        for i in range(len(lst)-1):
            if lst[i] >= lst[i+1]:
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


This code works by iterating through the list and checking if each element is greater than or equal to the next element. If it finds an element that is not greater than or equal to the next one, it returns False. If it doesn't find any such pair, it returns True.
The time complexity is O(n), where n is the length of the list.
"""

#Q2:
"""
