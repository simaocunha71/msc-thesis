    if a == b:
        return None
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        else:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        if a > b:
            return a
        else:
            return b
    elif isinstance(a, (int, float)) and isinstance(b, str):
        a_split = str(a).split('.')
        if a_split[0] > b:
            return a
        if a_split[0] < b:
            return b
        if a_split[1] is None:
            return None
        if b.count('.') == 0:
            return a_split[1]
        if a_split[1] > b:
            return a_split[1]
        else:
            return b
    elif isinstance(a, str) and isinstance(b, (int, float)):
        b_split = str(b).split('.')
        if a > b:
            return a
        if a < b:
            return b
        if b_split[1] is None:
            return None
        if a.count('.') == 0:
            return b_split[1]
        if a == b:
            return None
        else:
            return b_split[1]


