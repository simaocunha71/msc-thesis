def occurance_substring(s, sub):
    for i in range(len(s)):
        if s[i:i+len(sub)] == sub:
            return (sub, i, i+len(sub))
    return None