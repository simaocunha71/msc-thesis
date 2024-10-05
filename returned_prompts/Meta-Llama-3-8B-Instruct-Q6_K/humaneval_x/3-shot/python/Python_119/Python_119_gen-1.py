    def is_balanced(s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    open_parens = lst[0]
    close_parens = lst[1]
    if open_parens.count('(') != close_parens.count(')'):
        return 'No'
    if is_balanced(open_parens + close_parens):
        return 'Yes'
    return 'No'




