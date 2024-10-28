    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # if group has fewer elements than 3, add the last element to the start of the group.
    groups = [(groups[i] + groups[i + 1][:2]) if len(groups[i]) < 3 else groups[i] for i in range(len(groups))]
    return "".join(groups)
