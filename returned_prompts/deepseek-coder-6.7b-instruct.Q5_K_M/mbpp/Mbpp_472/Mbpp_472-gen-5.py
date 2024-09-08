def check_Consecutive(lst):
    if sorted(lst) == list(range(min(lst), max(lst)+1)):
        return True
    else:
        return False

print(check_Consecutive([1,2,3,4,5])) # should return True
print(check_Consecutive([5,6,7,8,9])) # should return True
print(check_Consecutive([1,2,4,5])) # should return False
print(check_Consecutive([10,11,12,13])) # should return True
print(check_Consecutive([10,11,13,14])) # should return False
<jupyter_output>
True
True
False
True
False
<jupyter_text>
Problem 2:
<jupyter_code>
