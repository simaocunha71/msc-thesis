    if len(lst) == 0 or len(lst) == 1:
        return True

    if len(lst) > 1:
        if lst[0] > lst[1]:
            return False
        else:
            return is_sorted(lst[1:])

    return False


