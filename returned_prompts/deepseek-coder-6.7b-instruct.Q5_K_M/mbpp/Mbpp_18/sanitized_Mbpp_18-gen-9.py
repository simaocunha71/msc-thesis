def remove_dirty_chars(s1, s2):
    for i in s2:
        if i in s1:
            s1 = s1.replace(i, '')
    return s1