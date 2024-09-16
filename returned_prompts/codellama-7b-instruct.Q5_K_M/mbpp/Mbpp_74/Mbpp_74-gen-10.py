"""
def is_samepatterns(colors, patterns):
    return len(colors) == len(patterns) and all(x == patterns[i % len(patterns)] for i, x in enumerate(colors))
"""
