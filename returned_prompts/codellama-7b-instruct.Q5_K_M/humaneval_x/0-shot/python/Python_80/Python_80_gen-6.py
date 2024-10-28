
    return len(s) < 3 or all(s[i] != s[i+1] and s[i] != s[i+2] for i in range(len(s)-2))


