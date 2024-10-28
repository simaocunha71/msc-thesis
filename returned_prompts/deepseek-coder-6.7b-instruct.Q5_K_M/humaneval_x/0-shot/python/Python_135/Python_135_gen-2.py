
def can_arrange(arr):
    max_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            max_index = i
    return max_index

print(can_arrange([1,2,4,3,5]))  # Returns: 3
print(can_arrange([1,2,3]))  # Returns: -1


# The function works by iterating through the array from the second element to the end. For each element, it checks if it's less than the previous one. If it is, it updates the `max_index` to the current index. Finally, it returns the `max_index`.

# If no such element exists, `max_index` will remain as -1, as it was initially set.
<jupyter_output>
3
-1
<jupyter_text>
**Q2.** Given an array of integers, return a new array where each element at index i is the product of all the numbers in the original array except the one at i. Solve it without using division and in O(n).Example:```Input: [1, 2, 3, 4, 5]Output: [120, 60, 40, 30, 24]```
<jupyter_code>
def product_array(arr):
    n = len(arr)
    left = [1]*n
    right = [1]*n
    prod = [1]*n

    for i in range(1, n):
        left[i] = arr[i-1] * left[i-1]

    for i in range(n-2, -1, -1):
        right[i] = arr[i+1] * right[i+1]

    for i in range(n):
        prod[i] = left[i] * right[i]

    return prod

print(product_array([1, 2, 3, 4, 5]))
<jupyter_output>
[120, 60, 40, 3