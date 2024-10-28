    words = s.split()
    apples = 0
    oranges = 0

    for word in words:
        if word == 'apples':
            apples = int(''.join(filter(str.isdigit, s)))
        elif word == 'oranges':
            oranges = int(''.join(filter(str.isdigit, s)))

    return n - apples - oranges


