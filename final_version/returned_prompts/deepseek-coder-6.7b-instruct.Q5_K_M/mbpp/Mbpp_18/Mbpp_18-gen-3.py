def remove_dirty_chars(s1, s2):
    for char in s2:
        if char in s1:
            s1 = s1.replace(char, '')
    return s1

assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'

