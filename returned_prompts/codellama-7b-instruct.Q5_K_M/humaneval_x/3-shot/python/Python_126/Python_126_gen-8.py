    if len(lst) == 1:
        return True
    else:
        if lst[0] > lst[1]:
            return False
        else:
            return is_sorted(lst[1:])


