
def check_greater(array, n):
    return all(i > n for i in array)

print(check_greater([1, 2, 3, 4, 5], 4))

# Output: False

# This function works by using the built-in all() function in Python, which returns True if all elements in the given iterable are true.
# In this case, it's checking if all elements in the array are greater than n. If any element is not greater than n, then it returns False.
<jupyter_output>
False
<jupyter_text>
Problem 3
<jupyter_code>
