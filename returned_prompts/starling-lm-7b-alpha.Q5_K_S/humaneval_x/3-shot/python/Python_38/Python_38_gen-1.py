    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    for i in range(len(groups)):
        if len(groups[i]) < 3:
            groups[i] += groups[i]
    return ''.join(groups)


