    apples = 0
    oranges = 0

    for i in range(len(s)):
        if s[i] == "a":
            apples += 1
        elif s[i] == "o":
            oranges += 1

    return n - apples - oranges


