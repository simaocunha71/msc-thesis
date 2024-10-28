def get_Inv_Count(arr):
    return merge_sort(arr)[1]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        left, left_inv = merge_sort(arr[:mid])
        right, right_inv = merge_sort(arr[mid:])
        merged, split_inv = merge(left, right)
        return merged, left_inv + right_inv + split_inv
def merge(left, right):
    merged = []
    split_inv = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inv += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, split_inv