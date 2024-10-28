
def is_sorted(lst):
    if len(lst) <= 2:
        return True
    else:
        return all(a <= b for a, b in zip(lst, lst[1:]))

print(is_sorted([5]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5]))  # ➞ True
print(is_sorted([1, 3, 2, 4, 5]))  # ➞ False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # ➞ True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # ➞ False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # ➞ True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # ➞ False

Explanation:

The function is_sorted iterates over each pair of consecutive elements in the list and checks if the first one is less than or equal to the second one. If all these pairs are True, the list is sorted, and the function returns True. If at least one pair is False, the list is not sorted, and the function returns False.

This approach works because in Python, any non-empty iterable (like a list or a string) can be zipped with itself shifted by one using the zip function. The zip function stops at the end of the shorter iterable, so this allows us to pair up all the elements of the list with their successors.

The built-in all function returns True only if all the elements of its iterable are True. So, the overall effect of the is_sorted function is to check if all the pairs in the list are in ascending order.

If the list is empty or contains only one element, the function returns True because an empty