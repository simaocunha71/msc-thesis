    new_str = []
    for i in s:
        if i not in c:
            new_str.append(i)
    return ''.join(new_str), ''.join(new_str) == ''.join(new_str[::-1])


