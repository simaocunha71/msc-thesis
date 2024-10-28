def check_min_heap(arr):
    n = len(arr)
    for i in range(n // 2, n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left >= n and right >= n:
            return True
        elif left >= n:
            if arr[i] < arr[right]:
                return True
            else:
                return False
        elif right >= n:
            if arr[i] < arr[left]:
                return True
            else:
                return False