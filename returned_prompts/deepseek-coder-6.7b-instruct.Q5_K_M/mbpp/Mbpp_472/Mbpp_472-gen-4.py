def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst)+1))

print(check_Consecutive([1,2,3,4,5]))

# It works by sorting the list and comparing it to a list of numbers from the smallest to largest in the original list. 
# If they are the same, then the original list had consecutive numbers, so it returns True. Otherwise, it returns False.
<jupyter_output>
True
<jupyter_text>
Question 2: Write a Python function to check whether the given list contains duplicate values or not.
<jupyter_code>
