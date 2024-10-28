def move_num(s):
    for i in range(len(s)):
        if not s[i].isalpha():
            s = s[:i] + s[i+1:]
    return s