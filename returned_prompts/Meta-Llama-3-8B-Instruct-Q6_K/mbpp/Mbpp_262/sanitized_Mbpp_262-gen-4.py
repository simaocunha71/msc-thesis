def split_two_parts(lst, L):
    return tuple(lst[:L], lst[L:]) if L <= len(lst) else (tuple(lst), [])  # Edge case: L is larger than the list size