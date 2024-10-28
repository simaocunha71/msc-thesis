def occurance_substring(s, substr):
    pos = s.find(substr)
    if pos != -1:
        return substr, pos, pos + len(substr)
    else:
        return None