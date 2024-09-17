
def number_of_substrings(s: str) -> int:
    return sum(1 for i in range(len(s)) for j in range(i + 1, len(s) + 1))


