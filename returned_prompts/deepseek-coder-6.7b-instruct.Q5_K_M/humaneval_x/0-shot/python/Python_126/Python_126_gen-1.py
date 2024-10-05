
def is_sorted(lst):
    if len(lst) == 1:
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
        if lst[i] == lst[i + 1]:
            return False
    return True

print(is_sorted([5]))  # True
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # False

Explanation:
This function checks each pair of adjacent elements in the list. If any pair is in ascending order, it continues to the next pair. If any pair is not in ascending order or has duplicates, it immediately returns False. If it checks all pairs without finding any out-of-order pairs, it returns True.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
3. Write a Python function to count the number of unique elements in a list.
<jupyter_code>
