    # O(n) time and O(n) space
    # we could do this in O(1) space and O(n) time, but this is simpler
    # this is a typical use case for two pointers
    # two pointers from the end, one from the beginning, and then we just iterate
    # until they meet
    left = 0
    right = len(arr) - 1
    changed = 0
    while left <= right:
        if arr[left] != arr[right]:
            changed += 1
            arr[left] = arr[right]
        left += 1
        right -= 1

    return changed


