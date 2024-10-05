
def next_smallest(lst):
    if len(lst) < 2:
        return None
    smallest = min(lst)
    lst.remove(smallest)
    if len(lst) < 1:
        return None
    next_smallest = min(lst)
    return next_smallest

print(next_smallest([1, 2, 3, 4, 5])) # 2
print(next_smallest([5, 1, 4, 3, 2])) # 2
print(next_smallest([])) # None
print(next_smallest([1, 1])) # None


# Alternative solution:

def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1]

print(next_smallest([1, 2, 3, 4, 5])) # 2
print(next_smallest([5, 1, 4, 3, 2])) # 2
print(next_smallest([])) # None
print(next_smallest([1, 1])) # None

This alternative solution sorts the list in ascending order and then returns the second element of the sorted list. The time complexity is O(n log n). The first solution removes the minimum element from the list and then finds the minimum again. This would be a bit more efficient if the list is large, as the time complexity would be O(n).
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4:Write a function that takes in a list of numbers and returns True if there is at least one pair of numbers in the list that add up to 0 and False otherwise.
<jupyter_code>
def has_zero_sum_pair(lst):
    """
    has_zero_sum_pair([1, 2, 3, -1]) ➞ True
    # Because 1+3=4 and 2+(-1)=1
    has_zero_sum_pair([1, 2, 3, 4]) 