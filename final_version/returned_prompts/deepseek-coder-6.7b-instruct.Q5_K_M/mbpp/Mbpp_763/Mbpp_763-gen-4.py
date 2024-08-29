def find_min_diff(arr,n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1,n):
        diff = arr[i] - arr[i-1]
        min_diff = min(min_diff, diff)
    return min_diff

print(find_min_diff((1,5,3,19,18,25),6))

# This function sorts the array and then iterates through the array comparing the differences between consecutive elements. The smallest difference found is returned.

# This code snippet works by first sorting the array. This is because we are looking for the minimum difference between any two elements, and a difference of 0 would be the minimum difference for two elements that are the same. 

# Then, it iterates through the array, calculating the difference between each pair of consecutive elements and updating the minimum difference found so far. 

# The time complexity of this solution is O(n log n) due to the sort operation, and the space complexity is O(1) because no additional space is used.
<jupyter_output>
1
<jupyter_text>
Question 2:
<jupyter_code>
