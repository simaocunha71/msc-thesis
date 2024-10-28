    neg = [x for x in lst if x < 0]
    pos = [x for x in lst if x > 0]
    return (max(neg) if neg else None, min(pos) if pos else None)


