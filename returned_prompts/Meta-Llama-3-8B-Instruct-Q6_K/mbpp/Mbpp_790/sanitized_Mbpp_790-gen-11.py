def even_position(lst):
    if len(lst) == 0:
        return True
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True