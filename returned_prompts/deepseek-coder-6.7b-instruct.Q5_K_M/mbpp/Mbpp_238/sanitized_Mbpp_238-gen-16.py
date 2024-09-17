def number_of_substrings(string: str) -> int:
    return sum(len(string[i:j]) for i in range(len(string)) for j in range(i + 1, len(string) + 1))