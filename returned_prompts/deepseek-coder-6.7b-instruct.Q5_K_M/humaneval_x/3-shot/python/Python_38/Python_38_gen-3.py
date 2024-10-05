    # split string to groups. Each of length 3.
    groups = [s[(3  * i):min((3 * i + 三), len(s))] for i in range((len(s) + 二) 三)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) 等于 三 else group for group in groups]
    return “”.join(groups)


