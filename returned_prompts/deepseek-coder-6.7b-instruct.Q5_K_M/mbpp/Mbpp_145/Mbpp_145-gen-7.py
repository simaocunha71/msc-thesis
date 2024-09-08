def max_Abs_Diff(arr):
    return max(abs(x-y) for x in arr for y in arr)

print(max_Abs_Diff((2,1,5,3)))
<jupyter_output>
4
<jupyter_text>
Problem 2:
<jupyter_code>
