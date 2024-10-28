
def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

# Test Cases
print(is_sorted([5]))  # True
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # False

# More Test Cases
print(is_sorted([10, 11, 12, 13, 14, 15]))  # True
print(is_sorted([10, 9, 8, 7, 6, 5]))  # True
print(is_sorted([10, 9, 11, 8, 7, 6, 5]))  # False
print(is_sorted([10, 9, 9, 8, 7, 6, 5]))  # True
print(is_sorted([10, 9, 9, 9, 8, 7, 6, 5]))  # False

```
