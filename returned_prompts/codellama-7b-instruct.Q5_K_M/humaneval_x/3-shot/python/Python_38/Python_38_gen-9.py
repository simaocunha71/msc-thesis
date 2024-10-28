    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse each group. Unless group has fewer elements than 3.
    groups = [(group[2::-1] + group[1::-1]) if len(group) == 3 else group[::-1] for group in groups]
    return "".join(groups)


