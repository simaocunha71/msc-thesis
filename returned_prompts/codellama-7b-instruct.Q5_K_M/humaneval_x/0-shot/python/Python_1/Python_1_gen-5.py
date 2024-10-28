    bal = 0
    output = []
    current = ''
    for c in paren_string:
        if c == '(':
            bal += 1
            current += c
        elif c == ')':
            bal -= 1
            current += c
        elif c == ' ':
            pass
        else:
            current += c
        if bal == 0 and current != '':
            output.append(current)
            current = ''
            bal = 0
    if current != '':
        output.append(current)
    return output
