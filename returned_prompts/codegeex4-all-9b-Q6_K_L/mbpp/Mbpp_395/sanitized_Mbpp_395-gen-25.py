def first_non_repeating_character(s):
    return next((c for c in s if s.count(c) == 1), None)