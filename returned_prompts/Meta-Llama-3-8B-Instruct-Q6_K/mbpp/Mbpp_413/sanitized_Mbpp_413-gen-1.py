def extract_nth_element(lst, n):
    return [x for i, x in enumerate(lst) if i == n] if n < len(lst) else None