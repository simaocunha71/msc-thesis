def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst)+1))

print(check_Consecutive([1,2,3,4,5])) # True

# Another way
def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst)+1))

print(check_Consecutive([1,2,3,4,5])) # True
"""

