    def is_palindrome(arr):
        return arr == arr[::-1]

    if is_palindrome(arr):
        return 0

    n = len(arr)
    min_changes = float('inf')

    for i in range(n // 2):
        changes = 0
        for j in range(i + 1, n - i):
            if arr[i] != arr[j]:
                changes += 1
        min_changes = min(min_changes, changes)

    return min_changes

