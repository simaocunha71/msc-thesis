def get_Inv_Count(arr):
    if len(arr) <= 1:
        return 0

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half_count = get_Inv_Count(left_half)
    right_half_count = get_Inv_Count(right_half)

    merged_count = merge_and_count(left_half, right_half)

    return left_half_count + right_half_count + merged_count
def merge_and_count(left, right):
    merged = []
    inv_count = 0
    i = j = 0

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