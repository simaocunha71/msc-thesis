    apples = 0
    oranges = 0

    for word in s.split():
        if word.split()[1] == "apples":
            apples = int(word.split()[0])
        elif word.split()[1] == "oranges":
            oranges = int(word.split()[0])

    return n - apples - oranges


