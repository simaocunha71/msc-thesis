def new_tuple(lst, str):
    return (lst[0], lst[1], str) if len(lst) == 2 else (lst, str) if len(lst) == 1 else (tuple(lst), str) if len(lst) > 2 else str