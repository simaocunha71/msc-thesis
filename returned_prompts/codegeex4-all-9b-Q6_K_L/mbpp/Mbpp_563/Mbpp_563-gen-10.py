def extract_values(s):
    values = []
    for i in range(len(s)):
        if s[i] == '"':
            j = i + 1
            while j < len(s) and s[j] != '"':
                j += 1
            values.append(s[i+1:j])
            i = j
    return values

