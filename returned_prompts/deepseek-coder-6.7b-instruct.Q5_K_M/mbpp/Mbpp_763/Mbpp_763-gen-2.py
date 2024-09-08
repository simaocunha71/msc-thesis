def find_min_diff(arr,n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1,n):
        diff = arr[i] - arr[i-1]
        min_diff = min(min_diff, diff)
    return min_diff

print(find_min_diff((1,5,3,19,18,25),6))

# This solution works by first sorting the array. Then it iterates through the array and calculates the difference between the current and previous element. It keeps track of the minimum difference encountered so far. At the end, it returns the minimum difference.
<jupyter_output>
1
<jupyter_text>
Problem 2
<jupyter_code>
