def first_non_repeating_character(s):
    return next(filter(lambda c: s.count(c) == 1, s), None)