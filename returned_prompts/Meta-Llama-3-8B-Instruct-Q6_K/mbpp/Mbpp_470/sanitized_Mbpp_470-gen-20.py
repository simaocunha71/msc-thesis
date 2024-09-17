def add_pairwise(t):
    result = ()
    for i in range(1, len(t)):
        result += (t[i-1] + t[i],)
    return result