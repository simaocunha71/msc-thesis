def find_min_diff(arr, target):
    if len(arr) < 2:
        return 0
    arr.sort()
    left, right = 0, 1
    min_diff = float('inf')
    while right < len(arr):
        diff = arr[right] - arr[left]
        if diff < min_diff:
            min_diff = diff
        if diff < target:
            right += 1
        else:
            left += 1
    return min_diff