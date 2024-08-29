def reverse_Array_Upto_K(arr, k):
    arr[:k] = arr[:k][::-1]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))

"""
The function reverse_Array_Upto_K takes two parameters, arr which is the array to be reversed and k which is the position upto which the array should be reversed.
We use slicing to reverse the array upto the position k and then return the array.
In the given example, the function returns [4, 3, 2, 1, 5, 6] which is the array after reversing upto the 4th position.
"""
<jupyter_output>
[4, 3, 2, 1, 5, 6]
<jupyter_text>
Question 4
<jupyter_code>
