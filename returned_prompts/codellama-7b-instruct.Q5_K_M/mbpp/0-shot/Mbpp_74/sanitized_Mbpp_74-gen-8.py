def is_samepatterns(patterns, strs):
    return all(x==y for x,y in zip(patterns, strs))