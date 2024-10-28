def number_of_substrings(s: str) -> int:
    if len(s) == 0:
        return 0
    return (len(s) * (len(s) + 1)) // 2

