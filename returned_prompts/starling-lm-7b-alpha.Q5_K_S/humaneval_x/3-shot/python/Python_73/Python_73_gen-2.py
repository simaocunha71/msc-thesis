    def count_changes(arr, mid):
        count = 0
        for i in range(mid):
            if arr[i] != arr[len(arr) - 1 - i]:
                count += 1
        return count

    def smallest_change(arr):
        if len(arr) == 1:
            return 0
        mid = len(arr) // 2
        left_min, right_min = count_changes(arr, mid), count_changes(arr[:mid], mid)
        return min(left_min, right_min, smallest_change(arr[:mid]), smallest_change(arr[mid:]))

    return smallest_change(arr)


