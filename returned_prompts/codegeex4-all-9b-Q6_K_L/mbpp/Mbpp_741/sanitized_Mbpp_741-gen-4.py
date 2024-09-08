def all_Characters_Same(s: str) -> bool:
    if len(s) <= 1:
        return True
    return all(c == s[0] for c in s)