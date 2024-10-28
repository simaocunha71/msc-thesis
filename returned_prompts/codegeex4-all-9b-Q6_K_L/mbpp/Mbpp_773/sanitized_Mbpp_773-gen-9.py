def occurance_substring(s, sub):
    i = s.find(sub)
    if i == -1:
        return None
    else:
        return (sub, i, i+len(sub)-1)