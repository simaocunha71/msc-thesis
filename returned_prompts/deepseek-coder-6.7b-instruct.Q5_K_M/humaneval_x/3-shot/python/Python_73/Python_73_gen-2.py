    def count_changes(left, right):
        if left >= right:
            return 0
        if arr[left] == arr[right]:
            return count_changes(left + 1, right - 1)
        else:
            return 1 + min(count_changes(left + 1, right), count_changes(left, right - 1))

    return count_changes(0, len(arr) - 1)

