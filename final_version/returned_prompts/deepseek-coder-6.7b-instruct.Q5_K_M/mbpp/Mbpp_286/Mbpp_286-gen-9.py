"""
The idea is to find the sum of the array and then find the max subarray sum. The max subarray sum is found by finding the min subarray sum and subtracting it from the total sum. The total sum is found by multiplying the sum of the array with k. The min subarray sum is found using the Kadane's algorithm.
"""

def max_sub_array_sum_repeated(arr, k):
    n = len(arr)
    
    total_sum = sum(arr)
    
    max_end = max_so_far = min_end = min_so_far = arr[0]
    for i in range(1, n*k):
        max_end = max(arr[i%n], max_end + arr[i%n])
        min_end = min(arr[i%n], min_end + arr[i%n])
        max_so_far = max(max_so_far, max_end)
        min_so_far = min(min_so_far, min_end)
    
    if total_sum == min_so_far:
        return max_so_far
    else:
        return max(max_so_far, total_sum - min_so_far)

print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))
"""
Explanation:
In the given array, the largest sum of a contiguous subarray is 30 which is formed by the subarray [10, 20]. The array is repeated 4 times.
"""
<jupyter_output>
30
<jupyter_text>
4. Find the shortest path in a Binary Maze
<jupyter_code>
