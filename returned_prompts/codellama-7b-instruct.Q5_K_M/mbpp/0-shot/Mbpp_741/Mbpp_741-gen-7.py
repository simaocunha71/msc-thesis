def all_Characters_Same(str):
    if len(str) == 0:
        return True
    first = str[0]
    for c in str[1:]:
        if c != first:
            return False
    return True
