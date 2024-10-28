def snake_to_camel(s):
    result = s[0].lower()
    for i in range(1, len(s)):
        if s[i] == '_':
            result += s[i+1].upper()
        else:
            result += s[i]
    return result