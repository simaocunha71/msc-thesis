    return [max(map(paren_string.count, '()')) for _ in range(len(paren_string.split(' ')))]
