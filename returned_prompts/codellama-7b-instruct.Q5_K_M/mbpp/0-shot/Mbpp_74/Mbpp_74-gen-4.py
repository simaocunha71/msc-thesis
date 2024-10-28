"""
def is_samepatterns(patterns, seq):
    for i, p in enumerate(patterns):
        if p not in seq[:i+1]:
            return False
    return True
"""
