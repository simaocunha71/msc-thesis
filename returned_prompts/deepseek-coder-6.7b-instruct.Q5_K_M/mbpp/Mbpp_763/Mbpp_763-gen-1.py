"""
def find_min_diff(arr, n):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(1, n):
        diff = arr[i] - arr[i - 1]
        min_diff = min(min_diff, diff)
    return min_diff

print(find_min_diff((1,5,3,19,18,25),6))
"""

