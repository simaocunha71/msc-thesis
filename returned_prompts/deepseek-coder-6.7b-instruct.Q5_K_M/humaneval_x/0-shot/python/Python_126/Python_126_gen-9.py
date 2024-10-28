
def is_sorted(lst):
    if len(lst) == 1:
        return True
    else:
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

In this solution, we iterate over the list of numbers. If we find a number that is greater than the next one, we immediately return False as that means the list is not sorted in ascending order. If we go through the entire list without finding such a pair of numbers, we return True to signify that the list is sorted in ascending order.
This solution also handles the case where the list has more than one duplicate of the same number by checking the order of the numbers, not their frequency.

'''

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

print(is_sorted([5]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5]))  # ➞ True
print