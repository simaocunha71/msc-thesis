    open_brackets = sum(1 for b in brackets if b == '<')
    closed_brackets = sum(1 for b in brackets if b == '>')
    return open_brackets == closed_brackets


