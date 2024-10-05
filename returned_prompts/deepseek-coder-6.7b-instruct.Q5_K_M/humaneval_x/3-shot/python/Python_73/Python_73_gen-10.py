    def count_changes(i, j):
        if i >= j: return 0
        if arr[i] == arr[j]: return count_changes(i+1, j-1)
        return 1 + min(count_changes(i+1, j), count_changes(i, j-1))

    return count_changes(0, len(arr) - 1)


