def occurance_substring(s, sub):
    pos = s.find(sub)
    if pos == -1:
        return None
    else:
        return (sub, pos, pos + len(sub) - 1)