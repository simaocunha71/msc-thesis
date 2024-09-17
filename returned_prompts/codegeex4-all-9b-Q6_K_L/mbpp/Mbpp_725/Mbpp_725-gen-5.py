def extract_quotation(s):
    q = []
    for i in range(len(s)):
        if s[i] == '"':
            j = i+1
            while j < len(s) and s[j] != '"':
                j += 1
            q.append(s[i+1:j])
            i = j
    return q