def number_of_substrings(s: str):
    n = len(s)
    return n * (n + 1) // 2

assert number_of_substrings("abc") == 6


