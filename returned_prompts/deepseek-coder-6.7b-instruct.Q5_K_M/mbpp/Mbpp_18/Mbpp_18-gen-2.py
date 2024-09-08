
def remove_dirty_chars(s1, s2):
    for ch in s2:
        if ch in s1:
            s1 = s1.replace(ch, '')
    return s1

print(remove_dirty_chars("probasscurve", "pros"))

