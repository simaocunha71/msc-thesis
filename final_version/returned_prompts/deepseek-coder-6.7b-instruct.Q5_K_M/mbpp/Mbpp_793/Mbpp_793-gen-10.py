def last(arr, ele):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == ele:
            return i
    return -1

print(last([1,2,3],1))

#Output: 0

"""
This function starts from the end of the array and moves towards the start, so it stops as soon as it finds the first match. It returns -1 if the element is not found.
"""
<jupyter_output>
0
<jupyter_text>
Question 2
<jupyter_code>
