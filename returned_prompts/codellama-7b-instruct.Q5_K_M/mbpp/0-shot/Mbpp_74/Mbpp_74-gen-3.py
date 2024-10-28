def is_samepatterns(patterns, strings):
    return all(pattern == strings[i] for i, pattern in enumerate(patterns))
