
def split_Arr(arr, n):
    return arr[n:] + arr[:n]

print(split_Arr([12,10,5,6,52,36],2))

"""
Explanation:
The given function takes a list and an integer as an argument. It splits the list at the nth index and adds the first part to the end.
"""
<jupyter_output>
[5, 6, 52, 36, 12, 10]
<jupyter_text>
