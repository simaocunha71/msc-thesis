    # split string to groups of three characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group, unless group has fewer elements than 3.
    groups = [group[0] + group[1:] if len(group) == 3 else group for group in groups]
    return "".join(groups)


