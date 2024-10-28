def occurance_substring(s, sub):
    if sub in s:
        start = s.find(sub)
        return (sub, start, start + len(sub))
    else:
        return None