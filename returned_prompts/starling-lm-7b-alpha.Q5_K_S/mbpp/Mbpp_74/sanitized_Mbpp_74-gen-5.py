def is_samepatterns(pattern1, pattern2):
    n1 = len(pattern1)
    n2 = len(pattern2)
    if n1 != n2:
        return False
    for i in range(n1):
        if pattern1[i] != pattern2[i]:
            return False
    return True