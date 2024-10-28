def is_samepatterns(patterns):
    for p in patterns:
        if len(p) != len(patterns[0]):
            return False
    return True