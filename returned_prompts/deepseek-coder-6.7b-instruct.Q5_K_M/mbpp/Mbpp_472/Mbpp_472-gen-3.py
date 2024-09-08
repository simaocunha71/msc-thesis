def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst)+1))

print(check_Consecutive([1,2,3,4,5]))  # True
print(check_Consecutive([5,4,3,2,1]))  # True
print(check_Consecutive([1,2,4,5]))    # False
print(check_Consecutive([1,1,2,3]))    # False
<jupyter_output>
True
True
False
False
<jupyter_text>
Q2. Write a python function to check whether the given list is palindrome or not.
<jupyter_code>
