def is_samepatterns(l1, l2):
    return len(set(zip(l1, l2))) == len(l1) == len(l2)