    if not lst:
        return []

    sorted_lst = sorted(lst)
    result = []
    left = 0
    right = len(sorted_lst) - 1

    while left <= right:
        result.append(sorted_lst[left])
        if left != right:
            result.append(sorted_lst[right])
        left += 1
        right -= 1

    return result

