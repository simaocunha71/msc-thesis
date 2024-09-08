def min_swaps(arr, k):
    n = len(arr)
    greater_than_k = 0
    for i in range(n):
        if arr[i] > k:
            greater_than_k += 1
    count = greater_than_k
    left = 0
    right = greater_than_k
    min_swaps = float('inf')
    while right < n:
        min_swaps = min(min_swaps, count)
        if arr[left] > k:
            count -= 1
        if arr[right] > k:
            count += 1
        left += 1
        right += 1
    min_swaps = min(min_swaps, count)
    return min_swaps

print(min_swaps([2, 7, 9, 5, 8, 7, 4], 6))
<jupyter_output>
2
<jupyter_text>
Q3:
<jupyter_code>
"""
Given an array of integers, write a python function to find the maximum length of a