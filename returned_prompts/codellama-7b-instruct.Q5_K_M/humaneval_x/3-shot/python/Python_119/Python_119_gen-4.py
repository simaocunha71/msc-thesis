    open_bracket = 0
    for i in lst[0]:
        if i == '(':
            open_bracket += 1
        else:
            open_bracket -= 1

    for j in lst[1]:
        if j == ')':
            open_bracket -= 1
        else:
            open_bracket += 1

    if open_bracket == 0:
        return 'Yes'
    else:
        return 'No'


