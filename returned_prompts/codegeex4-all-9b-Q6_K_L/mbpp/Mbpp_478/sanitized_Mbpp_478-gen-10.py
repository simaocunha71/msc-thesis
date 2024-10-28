def remove_lowercase(s: str) -> str:
    if not s:
        return ''
    result = []
    i = 0
    while i < len(s):
        if s[i].isupper():
            result.append(s[i])
            i += 1
        else:
            j = i + 1
            while j < len(s) and s[j].islower():
                j += 1
            i = j
    return ''.join(result)