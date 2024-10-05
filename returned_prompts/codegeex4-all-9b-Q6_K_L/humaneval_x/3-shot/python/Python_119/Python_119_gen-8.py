    count = 0
    for c in lst[0]:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1

    if count != 0:
        return 'No'

    count = 0
    for c in lst[1]:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1

    if count != 0:
        return 'No'

    return 'Yes'

