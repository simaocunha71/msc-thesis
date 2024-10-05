def same_chars(s0: str, s1: str):
    return sorted(s0) == sorted(s1)
    # or return len(set(s0)) == len(set(s1)) and set(s0) == set(s1)  # this is more efficient for large strings
    # or return sorted(s0) == sorted(s1) and len(s0) == len(s1)  # this is more efficient for large strings
    # or return s0.replace(' ', '').lower() == s1.replace(' ', '').lower()  # this is more efficient for small strings
    # or return s0.replace(' ', '').lower() == s1.replace(' ', '').lower().replace(' ', '').lower()  # this is more efficient for small strings
    # or return set([x for x in s0]) == set([x for x in s1])  # this is more efficient for large strings
    # or return sorted([x for x in s0]) == sorted([x for x in s1])  # this is more efficient for large strings
    # or return sorted([x for x in s0], key=lambda x: (x.lower(), x.isupper())) == sorted([x for x in s1], key=lambda x: (x.lower(), x.isupper()))  # this is more efficient for large strings
    # or return sorted([x for x in s0], key=lambda x: (x.lower(), x.isupper())) == sorted([x for x in s1], key=lambda x: (x.lower(), x.isupper()))  # this is more efficient for large strings
    # or return sorted([x for x in s0], key=lambda x: (x.lower(), x.isupper())) == sorted([x for x in s1], key=lambda x: (x.lower(), x.isupper()))  # this is more efficient for large strings
    # or return sorted([x for x in s0], key=lambda x: (x.lower(), x.isupper())) == sorted([x for x in s1], key=lambda x: (x.lower(), x.isupper()))  # this is more efficient for large strings
    # or return sorted([x for x in s0], key=lambda x: (x.lower(), x.isupper())) == sorted([x for x in s1], key=lambda x: (x.lower(), x.isupper()))  # this is more efficient for large strings
   