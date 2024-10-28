def find_substring(lst: list, sub: str) -> bool:
    for word in lst:
        if sub in word:
            return True
    return False