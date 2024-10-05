    if len(lst) == 1:
        return True
    else:
        if lst[1] < lst[0]:
            return False
        else:
            return is_sorted(lst[1:])


