def reverse_Array_Upto_K(arr, k):
    for i in range(k//2):
        arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4))

"""
Explanation:
The function reverse_Array_Upto_K takes an array and a number k as arguments.
It then uses a for loop to iterate through the array and swap the first and last elements, the second and second last elements, and so on until it reaches the middle of the array. The number of iterations is determined by k/2 because we are swapping pairs of elements.
Finally, it returns the modified array.
"""

# Time complexity: O(k)
# Space complexity: O(1)

# You can test it with other examples as well.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7) == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10]

# Also, the function will work with arrays of any length and with any value of k.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5], 3) == [3, 2, 1, 4, 5]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1]

# If k is greater than the length of the