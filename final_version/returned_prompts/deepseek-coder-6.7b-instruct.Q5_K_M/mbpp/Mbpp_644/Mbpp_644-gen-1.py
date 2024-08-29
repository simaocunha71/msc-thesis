
def reverse_Array_Upto_K(arr, k):
    arr[:k] = arr[:k][::-1]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))

# Output: [4, 3, 2, 1, 5, 6]

Explanation: 
The function takes an array and a number K as input. It then uses Python's list slicing to reverse the first K elements in the array. The [::-1] at the end of the slicing operation is used to reverse the list. Finally, it returns the modified array.

The time complexity of this solution is O(k) because slicing takes O(k) time. The space complexity is O(1) as no extra space is used.

"""

def reverse_Array_Upto_K(arr, k):
    arr[:k] = arr[:k][::-1]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))
"""

Output: [4, 3, 2, 1, 5, 6]

"""

def reverse_Array_Upto_K(arr, k):
    arr[:k] = arr[:k][::-1]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))
"""

Output: [4, 3, 2, 1, 5, 6]
"""
<jupyter_output>
[4, 3, 2, 1, 5, 6]
<jupyter_text>
Question 3:
<jupyter_code>
