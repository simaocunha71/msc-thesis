def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst)+1))

print(check_Consecutive([1,2,3,4,5]))  # True

"""
Explanation:
The function first sorts the list in ascending order. Then it compares the sorted list with a list that consists of all consecutive numbers between the minimum and maximum of the original list. If these two lists are equal, the function returns True, otherwise it returns False.
"""

