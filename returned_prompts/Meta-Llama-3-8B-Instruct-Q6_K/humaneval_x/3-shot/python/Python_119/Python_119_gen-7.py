    open_count = 0
    close_count = 0

    for parenthesis in lst[0]:
        if parenthesis == '(':
            open_count += 1
        elif parenthesis == ')':
            close_count += 1

    for parenthesis in lst[1]:
        if parenthesis == '(':
            open_count -= 1
        elif parenthesis == ')':
            close_count -= 1

    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'
