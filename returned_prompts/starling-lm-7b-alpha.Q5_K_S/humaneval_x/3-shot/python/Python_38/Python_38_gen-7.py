    # split string to groups of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group in reverse order.
    groups = [(group[0] + group[-1:][-2::-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


