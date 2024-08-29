def find_min_diff(arr, n):

    # Initialize difference as infinite
    diff = float('inf')

    # Sort array elements
    arr = sorted(arr)

    # Find the min diff by comparing adjacent pairs in sorted array
    for i in range(n-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]

    # Return min diff
    return diff

print(find_min_diff((1,5,3,19,18,25),6))

# Time complexity: O(n log n) due to sorting, where n is the number of elements in the array.
# Space complexity: O(1) since no additional space is required.
<jupyter_output>
1
<jupyter_text>
Problem 2
<jupyter_code>
