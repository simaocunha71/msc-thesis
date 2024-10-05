    if k == 0:
        return []
    elif k >= len(arr):
        return sorted(arr)
    else:
        max_k_elements = sorted(arr, reverse=True)[:k]
        return max_k_elements

