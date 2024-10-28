
def is_sorted(lst):
    # Check for duplicates
    if len(lst) != len(set(lst)):
        return False
    # Check for ascending order
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
