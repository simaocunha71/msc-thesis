def remove_dirty_chars(s1, s2):
    set_s2 = set(s2)
    return ''.join([c for c in s1 if c not in set_s2])  # or return ''.join(set(s1).difference(set(s2)))  # or return ''.join(filter(lambda c: c not in set_s2, s1))