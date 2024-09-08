def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))

"""
Explanation:
We are given an array and a number 'k'. We need to reverse the array upto 'k' elements.
The function 'reverse_Array_Upto_K' will take two arguments, the array and 'k'.
We will use Python's slicing feature to split the array into two parts: 
'arr[:k]' will be the part to be reversed and 'arr[k:]' will be the remaining part.
Then, we will use '[::-1]' to reverse the 'arr[:k]' part.
Finally, we will concatenate the reversed part and the remaining part 'arr[k:]' to get the desired result.
"""

# Test case 2:
arr = [1, 2, 3, 4, 5, 6]
k = 2
print(reverse_Array_Upto_K(arr, k)) # Output: [2, 1, 3, 4, 5, 6]

# Test case 3:
arr = [1, 2, 3, 4, 5, 6]
k = 6
print(reverse_Array_Upto_K(arr, k)) # Output: [6, 5, 4, 3, 2, 1]

# Test case 4:
arr = [1, 2, 3, 4, 5, 6]
k = 1
print(reverse_Array_Upto_K(arr, k)) # Output: [1, 2, 3, 4, 5, 6]

# Test case 5:
arr = [1, 2, 3, 4, 5, 6]
k = 3
print(reverse_Array_Upto_K(arr, k)) # Output: [3, 2, 1, 4, 5, 6]
<jupyter_