    def find_smallest(start, end):
        if start == end:
            return 0
        count = 0
        for i in range(start, end + 1):
            if arr[i] != arr[end]:
                count += 1
        return count

    def smallest_change(arr):
        start = 0
        end = len(arr) - 1
        min_changes = find_smallest(start, end)
        while start < end:
            if arr[start] != arr[end]:
                min_changes = min(min_changes, find_smallest(start + 1, end - 1))
            start += 1
            end -= 1
        return min_changes


