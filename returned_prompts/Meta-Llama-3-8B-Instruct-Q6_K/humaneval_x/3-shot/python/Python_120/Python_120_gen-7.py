    return sorted(arr, reverse=True)[:k] if k <= len(arr) else []
    # or return sorted(set(arr), reverse=True)[:k] if you want to remove duplicates
    # or return sorted(set([x for x in arr if x > 0]), reverse=True)[:k] if you want to return only positive numbers


