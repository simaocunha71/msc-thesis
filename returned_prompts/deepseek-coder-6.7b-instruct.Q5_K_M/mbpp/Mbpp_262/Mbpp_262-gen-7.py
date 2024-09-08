def split_two_parts(lst, L):
    return (lst[:L], lst[L:])

print(split_two_parts([1,1,2,3,4,4,5,1],3)) # Expected output: ([1, 1, 2], [3, 4, 4, 5, 1])

# Solution 2
"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple. If the length of the list is less than L, the function should return the original list and a message "List too short".
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
assert split_two_parts([1,1,2,3,4,4,5,1],10)=="List too short"
"""

def split_two_parts(lst, L):
    if len(lst) < L:
        return "List too short"
    else:
        return (lst[:L], lst[L:])

print(split_two_parts([1,1,2,3,4,4,5,1],3)) # Expected output: ([1, 1, 2], [3, 4, 4, 5, 1])
print(split_two_parts([1,1,2,3,4,4,5,1],10)) # Expected output: "List too short"

# Solution 3
"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple. If the length of the list is less than L, the function should return the original list and a message "List too short". The function should also handle the case where L is negative by returning the original list and a message "Invalid input".
assert split_two_parts([1,1,2,