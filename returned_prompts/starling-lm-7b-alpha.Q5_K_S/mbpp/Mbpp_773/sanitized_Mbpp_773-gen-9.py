def occurance_substring(s, sub):
    result = []
    for i in range(len(s)):
        if s[i:i+len(sub)] == sub:
            result.append((sub, i, i+len(sub)-1))
    if result:
        return result[0]
    else:
        return None