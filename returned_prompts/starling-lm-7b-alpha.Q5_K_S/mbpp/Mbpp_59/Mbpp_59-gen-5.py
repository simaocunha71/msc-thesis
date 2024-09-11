def permutation_generator(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    ret = []
    for i in range(len(s)):
        c = s[i]
        rest = s[:i] + s[i+1:]
        for p in permutation_generator(rest):
            ret.append(c + p)