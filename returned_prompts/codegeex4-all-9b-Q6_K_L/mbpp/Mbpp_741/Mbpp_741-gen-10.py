def all_Characters_Same(s: str) -> bool:
    for i in range(1, len(s)):
        if s[i] != s[0]:
            return False
    return True

