
def count_reverse_pairs(strings: list) -> int:
    return len([s for s in strings if s == s[::-1]])


