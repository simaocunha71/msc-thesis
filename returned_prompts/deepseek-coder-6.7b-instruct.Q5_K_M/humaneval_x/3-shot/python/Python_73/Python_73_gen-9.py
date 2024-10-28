    def count_changes(left, right):
        changes = 0
        while left < right:
            if arr[left] != arr[right]:
                changes += 1
            left += 1
            right -= 1
        return changes

    return min(count_changes(0, len(arr) - 1), count_changes(1, len(arr)))


