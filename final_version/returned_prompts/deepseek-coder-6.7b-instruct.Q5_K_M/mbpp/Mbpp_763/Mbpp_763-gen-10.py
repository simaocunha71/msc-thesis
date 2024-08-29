def find_min_diff(arr, n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, n):
        diff = arr[i] - arr[i - 1]
        min_diff = min(min_diff, diff)
    return min_diff

print(find_min_diff((1,5,3,19,18,25),6))

# Output: 1

# This function works by first sorting the array in ascending order. It then iterates through the array to find the smallest difference between any two adjacent elements. The smallest difference is then returned as the result.
<jupyter_output>
1
<jupyter_text>
Question 2
<jupyter_code>
