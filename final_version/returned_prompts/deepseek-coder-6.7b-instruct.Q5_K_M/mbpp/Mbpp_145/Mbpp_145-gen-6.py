
def max_Abs_Diff(arr):
    return max(abs(x - y) for x in arr for y in arr)

print(max_Abs_Diff((2,1,5,3))) #== 4

# OR

def max_Abs_Diff(arr):
    return max(arr) - min(arr)

print(max_Abs_Diff((2,1,5,3))) #== 4

"""
This function works by taking the difference of each element in the array with every other element and taking the maximum of these differences.

In the second approach, it simply finds the maximum and the minimum value in the array and returns their difference. This will give the maximum absolute difference between any two elements in the array.
"""
<jupyter_output>
4
4
<jupyter_text>
Question 2
<jupyter_code>
"""
