def check_Consecutive(lst):
    if sorted(lst) == list(range(min(lst), max(lst)+1)):
        return True
    else:
        return False