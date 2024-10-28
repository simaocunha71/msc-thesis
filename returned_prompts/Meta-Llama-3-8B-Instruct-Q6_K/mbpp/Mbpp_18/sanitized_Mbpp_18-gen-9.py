def remove_dirty_chars(s1, s2):
    return "".join([c for c in s1 if c not in s2])  # or use s1.translate(str.maketrans('', '', s2)) for python 3.7+