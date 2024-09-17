def max_length(lsts):
    if len(lsts) == 0:
        return (0, [])
    else:
        return (len(lsts[0]), lsts[0]) if len(lsts[0]) > max_length(lsts[1:])[0] else max_length(lsts[1:])