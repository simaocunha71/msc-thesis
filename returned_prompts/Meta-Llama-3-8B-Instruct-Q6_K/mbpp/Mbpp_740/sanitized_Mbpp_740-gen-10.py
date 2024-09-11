def tuple_to_dict(tup):
    if len(tup) % 2 != 0:
        raise ValueError("Tuple length must be even")
    return {tup[i]: tup[i+1] for i in range(0, len(tup), 2)}