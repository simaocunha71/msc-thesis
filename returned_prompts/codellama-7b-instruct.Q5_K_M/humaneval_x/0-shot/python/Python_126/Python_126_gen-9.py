
def is_sorted(lst):
    if len(lst) == 0:
        return True
    if len(lst) == 1:
        return True

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True
