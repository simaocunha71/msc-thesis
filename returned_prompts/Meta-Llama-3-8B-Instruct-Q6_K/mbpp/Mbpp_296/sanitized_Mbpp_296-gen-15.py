def get_Inv_Count(arr):
    n = len(arr)
    if n == 1:
        return 0
    else:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        leftInvCount = get_Inv_Count(left)
        rightInvCount = get_Inv_Count(right)
        mergedInvCount = merge_and_count(left, right)
        return leftInvCount + rightInvCount + mergedInvCount
def merge_and_count(left, right):
    merged = []
    invCount = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            invCount += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return invCount