    def count_changes(left, right):
        c = 0
        while left < right:
            if arr[left] != arr[right]:
                c += 1
            left += 1
            right -= 1
        return c

    return min(count_changes(0, len(arr) - 1), count_changes(0, len(arr) - 2) + 1,
               count_changes(1, len(arr) - 1) + 1)


