def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst) + 1))

print(check_Consecutive([1,2,3,4,5])) # True

Explanation:
First, we sort the list. Then we create a list of numbers from the smallest to the largest number in the list. If these two lists are the same, then the original list has consecutive numbers, and the function returns True. If not, it returns False.
"""

#Solution:

def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst) + 1))

print(check_Consecutive([1,2,3,4,5])) # True

# Test cases
assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([2,3,4,5,6]) == True
assert check_Consecutive([1,2,4,5]) == False
assert check_Consecutive([1]) == True
assert check_Consecutive([]) == True
"""
"""
