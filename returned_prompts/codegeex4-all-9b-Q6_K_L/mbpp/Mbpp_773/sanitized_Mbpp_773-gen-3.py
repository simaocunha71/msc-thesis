def occurance_substring(s, sub):
    if sub in s:
        return sub, s.index(sub), s.rindex(sub)
    else:
        return None