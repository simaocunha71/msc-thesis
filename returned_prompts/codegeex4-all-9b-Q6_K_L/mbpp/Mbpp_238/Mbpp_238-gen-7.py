def number_of_substrings(s: str) -> int:
    if not s:
        return 0
    return sum(range(len(s) + 1))