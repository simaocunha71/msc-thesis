    if value.is_integer():
        return int(value)

    if value.startswith('-'):
        return int(value.split('.')[0]) - 1

    return int(value.split('.')[0]) + 1
