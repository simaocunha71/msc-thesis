def is_samepatterns(patterns, colors):
    if len(patterns) != len(colors):
        return False
    for i in range(len(patterns)):
        if patterns[i] != colors[i]:
            return False
    return True