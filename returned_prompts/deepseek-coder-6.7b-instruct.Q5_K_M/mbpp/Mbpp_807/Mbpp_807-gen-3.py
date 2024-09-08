def first_odd(nums):
    for num in nums:
        if num % 2 != 0:
            return num
    return None

print(first_odd([1,3,5]))
<jupyter_output>
1
<jupyter_text>
Problem 2
<jupyter_code>
