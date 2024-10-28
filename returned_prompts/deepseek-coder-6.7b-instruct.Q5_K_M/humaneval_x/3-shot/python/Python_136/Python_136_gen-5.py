    neg_integers = [i for i in lst if isinstance(i, int) and i < 0]
    pos_integers = [i for i in lst if isinstance(i, int) and i > 0]

    return (max(neg_integers) if neg_integers else None, min(pos_integers) if pos_integers else None)


