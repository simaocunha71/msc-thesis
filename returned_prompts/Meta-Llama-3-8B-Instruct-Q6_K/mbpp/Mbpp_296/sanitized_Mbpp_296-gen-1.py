def get_Inv_Count(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_count = get_Inv_Count(left)
    right_count = get_Inv_Count(right)
    split_count = merge_split_count(left, right)
    return left_count + right_count + split_count
def merge_split_count(left, right):
    inv_count = 0
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return inv_count