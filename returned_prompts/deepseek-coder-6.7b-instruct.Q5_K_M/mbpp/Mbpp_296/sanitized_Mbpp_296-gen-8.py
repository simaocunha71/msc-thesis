def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])
    merged, merge_inv = merge(left, right)
    total_inv = left_inv + right_inv + merge_inv

    return merged, total_inv
def merge(left, right):
    merged = []
    inversions = 0
    while left and right:
        if left[0] <= right[0]:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            right = right[1:]
            inversions += len(left)
    merged.extend(left if left else right)
    return merged, inversions
def get_Inv_Count(arr):
    _, inversions = merge_sort(arr)
    return inversions