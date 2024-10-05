
def solve(s):
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
        else:
            s[i] = s[i]
    return ''.join(s)

