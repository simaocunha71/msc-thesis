def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst)+1))

print(check_Consecutive([1,2,3,4,5])) # True
print(check_Consecutive([5,4,3,2,1])) # True
print(check_Consecutive([1,3,5,7,9])) # True
print(check_Consecutive([1,2,4,5,7])) # False
print(check_Consecutive([3,2,1,5,4])) # False
print(check_Consecutive([2,3,4,6,1])) # False
print(check_Consecutive([1])) # True
print(check_Consecutive([])) # True


"""
The function check_Consecutive works by first sorting the list and then checking if the sorted list is a range of numbers from the minimum to the maximum of the original list. If it is, the function returns True, otherwise it returns False.
"""
<jupyter_output>
True
True
True
False
False
False
True
True
<jupyter_text>
Question 2
<jupyter_code>
