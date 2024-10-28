def occurance_substring(s, sub):
    if sub in s:
        return (sub, s.index(sub), s.index(sub) + len(sub))
    return None