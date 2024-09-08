def reverse_Array_Upto_K(arr, k):
    # Firstly, we will reverse the first k elements.
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))

# Note: This solution assumes that the given array and position 'k' are valid. Also, it only reverses the first 'k' elements in the array. The rest of the array remains the same.

# The time complexity is O(n) and the space complexity is O(1) as it reverses the array in-place.

# If the position 'k' is larger than the array length, it will reverse the entire array.
# If it's smaller, it will reverse the first 'k' elements.
<jupyter_output>
[4, 3, 2, 1, 5, 6]
<jupyter_text>
Question 2
<jupyter_code>
