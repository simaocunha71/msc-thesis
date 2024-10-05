    open = 0

    for c in lst[0]:
        if c == '(':
            open += 1
        else:
            open -= 1

    for c in lst[1]:
        if c == '(':
            open += 1
        else:
            open -= 1

    return open == 0

