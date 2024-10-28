def get_Inv_Count(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_count = get_Inv_Count(left)
    right_count = get_Inv_Count(right)
    merged_count = merge_and_count(left, right)
    return left_count + right_count + merged_count
def merge_and_count(left, right):
    merged = []
    i = j = count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return count