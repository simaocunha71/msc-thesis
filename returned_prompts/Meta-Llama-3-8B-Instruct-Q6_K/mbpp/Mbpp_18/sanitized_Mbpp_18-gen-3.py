def remove_dirty_chars(s1, s2):
    return ''.join([c for c in s1 if c not in s2])
    # or return ''.join(set(s1) - set(s2))  # This will also work