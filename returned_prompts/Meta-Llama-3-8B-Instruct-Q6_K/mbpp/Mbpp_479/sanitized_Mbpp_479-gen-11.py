def first_Digit(n):
    s = str(n)
    for i in range(len(s)):
        if s[i].isdigit():
            return int(s[i])