    open_parens = 0
    close_parens = 0

    for c in lst[0]:
        if c == '(':
            open_parens += 1
        else:
            close_parens += 1

    for c in lst[1]:
        if c == '(':
            open_parens += 1
        else:
            close_parens += 1

    if open_parens == close_parens:
        return 'Yes'
    else:
        return 'No'  # Not balanced
    # if open_parens > close_parens, we need more ')'
    # if close_parens > open_parens, we need more '('
    # In both cases, the string is not good.  # Not good


