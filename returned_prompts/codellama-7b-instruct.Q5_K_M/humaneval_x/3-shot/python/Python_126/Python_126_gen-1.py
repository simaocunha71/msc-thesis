    if len(lst) == 1:
        return True
    elif len(lst) == 0:
        return False
    elif len(lst) >= 2:
        if lst[1] < lst[0]:
            return False
        else:
            if lst[1] == lst[0]:
                lst.pop(0)
                return is_sorted(lst)
            else:
                return is_sorted(lst)


