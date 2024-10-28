def snake_to_camel(s):
    s = s.split('_')
    for i in range(1, len(s)):
        s[i] = s[i].capitalize()
    return ''.join(s)