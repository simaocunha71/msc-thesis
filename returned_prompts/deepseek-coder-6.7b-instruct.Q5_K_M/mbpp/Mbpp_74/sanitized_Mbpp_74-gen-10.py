def is_samepatterns(colors, patterns):
    return colors[1:] == [patterns[i] for i in range(1, len(patterns))]