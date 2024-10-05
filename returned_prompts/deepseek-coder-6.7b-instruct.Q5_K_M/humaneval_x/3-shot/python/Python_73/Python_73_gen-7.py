    def count_changes(left, right):
        change = 0
        while left < right:
            if arr[left] != arr[right]:
                change += 1
            left += 1
            right -= 1
        return change

    return min(count_changes(0, len(arr) - 1), count_changes(1, len(arr)))


