def max_difference(lst):
    return max(b-a for a, b in lst) - min(b-a for a, b in lst) if lst else None