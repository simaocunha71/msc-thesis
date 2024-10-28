def odd_position(lst):
    if len(lst) < 2:
        return True
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True