def split_two_parts(lst, L):
    return (lst[:L], lst[L:]) if L <= len(lst) else (lst, [])  # if L is greater than the length of the list, return the original list and an empty list