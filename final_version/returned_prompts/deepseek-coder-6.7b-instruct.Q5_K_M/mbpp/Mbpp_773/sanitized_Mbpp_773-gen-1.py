def occurance_substring(s, sub):
    position = s.find(sub)
    if position != -1:
        return (sub, position, position+len(sub))
    else:
        return None