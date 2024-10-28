    apples = int(s[:s.find(' ')])
    oranges = int(s[s.find(' ') + 1:])
    return n - apples - oranges


