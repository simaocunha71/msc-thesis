    stack = []
    open_parens = 0
    res = []
    for c in paren_string:
        if c == '(':
            open_parens += 1
        elif c == ')':
            open_parens -= 1
        if open_parens == 0:
            res.append(paren_string[:open_parens + 1])
            paren_string = paren_string[open_parens + 1:]
            open_parens = 0
    return res


# print(separate_paren_groups('( ) (( )) (( )( ))'))


# print(separate_paren_groups('(((())))'))


# print(separate_paren_groups('( )( )'))


# print(separate_paren_groups('((( )( )))))'))


# print(separate_paren_groups('( () ())'))


# print(separate_paren_groups('(((())))'))


# print(separate_paren_groups('( )( )'))


# print(separate_paren_groups('((( )( )))))'))


# print(separate_paren_groups('( () ())'))


# print(separate_paren_groups('((( )( )))))'))


# print(separate_paren_groups('( () ())'))


# print(separate_paren_groups('((( )( )))))'))


# print(separate_paren_groups('( () ())'))


# print(separate_paren_groups('((( )( )))))'))


# print(separate_paren_groups('( () ())'))


# print(separate_paren_groups('((( )( )))))'))


# print(separate_paren_groups('( () ())'))


# print(separate_paren_groups('((( )( )))))'))


# print(separate_paren_groups('( () ())'))


# print(separate_paren_groups('((( )( )))))'))


# print(separate_paren_groups('( () ())'))