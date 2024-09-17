
def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst) + 1))


