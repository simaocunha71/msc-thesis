def heap_sort(arr):
    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        end -= 1
        sift_down(arr, 0, end)
    return arr
def sift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        swap = root
        if arr[swap] < arr[child]:
            swap = child
        if child + 1 <= end and arr[swap] < arr[child + 1]:
            swap = child + 1
        if swap != root:
            arr[root], arr[swap] = arr[swap], arr[root]
            root = swap
        else:
            return