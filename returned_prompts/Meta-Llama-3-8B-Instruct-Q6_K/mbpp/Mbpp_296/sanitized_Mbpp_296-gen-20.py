def get_Inv_Count(arr):
    n = len(arr)
    if n < 2:
        return 0
    else:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        left_count = get_Inv_Count(left)
        right_count = get_Inv_Count(right)
        merged_count = merge_and_count(left, right)
        return left_count + right_count + merged_count
def merge_and_count(left, right):
    merged = []
    i = j = inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_count += len(left) - i
    merged += left[i:]
    merged += right[j:]
    return inv_count