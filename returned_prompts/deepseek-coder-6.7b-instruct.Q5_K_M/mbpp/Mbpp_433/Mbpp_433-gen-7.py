def check_greater(arr, num):
    return all(i > num for i in arr)

print(check_greater([1, 2, 3, 4, 5], 4))

# This will return False as 4 is not greater than all elements in the array.
<jupyter_output>
False
<jupyter_text>
Question 2
<jupyter_code>
