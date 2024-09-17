def remove_dirty_chars(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    for c in s2:
        s1 = s1.replace(c, "")
    return s1