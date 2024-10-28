
def is_samepatterns(patterns, seq):
    return all(p == seq[i % len(p)] for i, p in enumerate(patterns))


