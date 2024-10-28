def is_majority(arr, n, el):
    for i in range(n):
        if arr[i] == el:
            count = 1
            while i < n - 1 and arr[i+1] == el:
                count += 1
                i += 1
            if count > n // 2:
                return True
    return False