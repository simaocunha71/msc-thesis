def heap_sort(lst):
    def sift_down(arr, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end: break
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] >= arr[child]: break
            arr[root], arr[child] = arr[child], arr[root]
            root = child

    n = len(lst)
    for start in range(n // 2 - 1, -1, -1):
        sift_down(lst, start, n - 1)
    for end in range(n - 1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        sift_down(lst, 0, end - 1)
    return lst