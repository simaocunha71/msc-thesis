def first_non_repeating_character(s: str):
    for i in s:
        if s.count(i) == 1:
            return i
    return None