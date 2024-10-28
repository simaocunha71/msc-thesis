def check_min_heap(arr: list) -> bool:
    def is_min_heap(arr, i, size):
        if i >= size:
            return True
        left = 2 * i + 1
        right = 2 * i + 2
        if left < size and arr[left] < arr[i]:
            return False
        if right < size and arr[right] < arr[i]:
            return False
        return is_min_heap(arr, left, size) and is_min_heap(arr, right, size)
    return is_min_heap(arr, 0, len(arr))