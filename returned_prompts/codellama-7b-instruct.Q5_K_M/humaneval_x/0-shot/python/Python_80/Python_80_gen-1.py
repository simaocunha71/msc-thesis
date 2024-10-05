
def is_happy(s):
    return len(s) >= 3 and all(s[i] != s[i+1] for i in range(len(s)-2))