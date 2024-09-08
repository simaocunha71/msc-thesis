def reverse_Array_Upto_K(arr, k):
    arr[:k] = arr[:k][::-1]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))

"""
Explanation:
The function reverse_Array_Upto_K takes two parameters, an array arr and a number k.
The array arr is sliced from 0 to k, and then reversed with the slice assignment.
The reversed sliced array is then returned.
"""
<jupyter_output>
[4, 3, 2, 1, 5, 6]
<jupyter_text>
Question 3:
<jupyter_code>
