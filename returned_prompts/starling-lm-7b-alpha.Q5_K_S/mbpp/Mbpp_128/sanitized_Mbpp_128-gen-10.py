def long_words(n,s):
    res = []
    for w in s.split():
        if len(w) > n:
            res.append(w)
    return res