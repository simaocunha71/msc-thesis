
def solve(s):
    if not any(char.isalpha() for char in s):
        return s[::-1]
    else:
        return ''.join([char.upper() if char.islower() else char.lower() for char in s])

print(solve("1234"))  # "4321"
print(solve("ab"))  # "AB"
print(solve("#a@C"))  # "#A@c"
print(solve("QwErTy"))  # "qWeRTy"

# In the above function, we first check if there are any letters in the string using any() and isalpha() function. 
# If not, we return the reversed string. If so, we convert each character to its opposite case using the lower() and upper() function, 
# and join them into a string using the join() function.
<jupyter_output>
4321
AB
#A@c
qWeRTy
<jupyter_text>
Question 2Given a list of integers, return the sum of the list. However, if the sum is greater than 10, return 20 instead. If the sum is less than or equal to 10, return the actual sum.Examples:```sum_list([1, 2, 3]) ➞ 6sum_list([5, 7, 5]) ➞ 20sum_list([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) ➞ 20```
<jupyter_code>
