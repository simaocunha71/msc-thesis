
def is_sorted(lst):
    if len(lst) < 2:
        return True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

#   This solution is O(n) time and O(1) space.
