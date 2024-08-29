"""
Here is a simple solution using python. The function first sorts the array in ascending order, then it iterates through the sorted array to find the minimum difference.
"""

def find_min_diff(arr,n):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        min_diff = min(min_diff, diff)
    return min_diff

print(find_min_diff((1,5,3,19,18,25),6)) # 1
"""
This function works by first sorting the input list `arr`, then iterating over the sorted list. In each iteration, it calculates the difference between the current element and the previous element, and updates `min_diff` if this difference is smaller than the current `min_diff`. 

Finally, it returns `min_diff`, which is the smallest difference between any two elements in the input list.
"""

# Time complexity: O(n log n) for the sort operation, O(n) for the iteration over the sorted array.
# Space complexity: O(n) for the sorted array.

# Note: This function assumes that the input list `arr` contains at least two elements. If this is not the case, the function may not work correctly.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 12: Write a Python program to find the sum of all elements in a list using recursion.
<jupyter_code>
