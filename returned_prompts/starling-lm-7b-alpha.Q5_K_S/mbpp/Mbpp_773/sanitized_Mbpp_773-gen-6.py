def occurance_substring(s, substr):
    if substr in s:
        return (substr, s.index(substr), s.index(substr) + len(substr))
    else:
        return None