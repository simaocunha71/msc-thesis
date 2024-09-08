def occurance_substring(s, sub):
    if sub not in s:
        return None
    else:
        return (sub, s.find(sub), s.rfind(sub))