def first_repeated_char(s):
    for i in s:
        if s.count(i) > 1:
            return i
    return "None"