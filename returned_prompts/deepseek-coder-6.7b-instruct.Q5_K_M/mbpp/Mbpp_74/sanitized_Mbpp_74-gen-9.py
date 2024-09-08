def is_samepatterns(colors, patterns):
    return all(patterns[i] == patterns[i + 1] for i in range(len(patterns) - 1))