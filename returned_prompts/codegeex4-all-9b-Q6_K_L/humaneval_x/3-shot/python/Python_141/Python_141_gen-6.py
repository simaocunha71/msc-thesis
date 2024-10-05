    digits = 0
    for c in file_name:
        if c.isdigit():
            digits += 1
        elif c == '.':
            break
    else:
        return 'No'

    if digits > 3:
        return 'No'

    if not file_name[:file_name.index('.')].isalpha():
        return 'No'

    if file_name[file_name.index('.') + 1:] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

