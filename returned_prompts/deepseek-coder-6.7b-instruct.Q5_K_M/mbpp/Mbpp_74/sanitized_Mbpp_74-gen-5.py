def is_samepatterns(colors, patterns):
    return len(set(zip(colors, patterns))) == 1