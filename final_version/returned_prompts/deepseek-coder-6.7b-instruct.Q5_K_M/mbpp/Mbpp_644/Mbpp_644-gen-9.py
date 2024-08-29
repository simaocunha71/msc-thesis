def reverse_Array_Upto_K(arr, k):
    arr[:k] = arr[:k][::-1]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))

# Solution by: Shubham Lodha
<jupyter_output>
[4, 3, 2, 1, 5, 6]
<jupyter_text>
Question 2
<jupyter_code>
