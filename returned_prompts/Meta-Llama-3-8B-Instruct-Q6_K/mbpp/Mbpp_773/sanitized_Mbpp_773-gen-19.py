def occurance_substring(s, sub):
    index = s.find(sub)
    if index == -1:
        return None
    return (sub, index, index + len(sub) - 1)