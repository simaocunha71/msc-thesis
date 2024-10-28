def first_non_repeating_character(s: str) -> str:
    if len(set(s)) == 1:
        return s[0]
    for i in s:
        if s.count(i) == 1:
            return i
    return None