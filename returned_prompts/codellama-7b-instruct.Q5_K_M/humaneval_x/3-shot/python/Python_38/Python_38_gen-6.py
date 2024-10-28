    # split string to groups of 3.
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[0] + group[2:] + group[1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


