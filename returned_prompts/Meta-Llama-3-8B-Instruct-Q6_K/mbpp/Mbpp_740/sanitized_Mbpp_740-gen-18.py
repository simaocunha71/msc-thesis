def tuple_to_dict(t):
    if len(t) == 0:
        return {}
    if len(t) % 2 != 0:
        raise ValueError("Tuple length must be even")
    return {t[i]: t[i+1] for i in range(0, len(t), 2)}