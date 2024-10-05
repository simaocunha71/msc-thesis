    return [x for n, x in sorted(enumerate(l), key=lambda pair: pair[0] if pair[0] % 3 == 0 else len(l))]

