def is_samepatterns(patterns1, patterns2):
    return all(patterns1[i] == patterns2[i] for i in range(len(patterns1)))