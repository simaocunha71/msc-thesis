    def changes_needed(start, end):
        c = 0
        while start < end:
            if arr[start] != arr[end]:
                c += 1
            start += 1
            end -= 1
        return c

    return min(changes_needed(0, len(arr) - 1), changes_needed(1, len(arr)))


