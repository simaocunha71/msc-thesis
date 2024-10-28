
def is_sorted(lst):
    # Check that the list is sorted
    if lst == sorted(lst):
        # Check for duplicates
        if len(lst) == len(set(lst)):
            return True
    return False