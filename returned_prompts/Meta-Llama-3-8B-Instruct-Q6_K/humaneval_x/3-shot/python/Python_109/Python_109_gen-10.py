    if not arr:
        return True

    last = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        if arr[i - 1] > last:
            return False
        last = arr[i - 1]

    return True
# Time complexity: O(n)
# Space complexity: O(1)  # since we're not using any extra space that scales with input size


