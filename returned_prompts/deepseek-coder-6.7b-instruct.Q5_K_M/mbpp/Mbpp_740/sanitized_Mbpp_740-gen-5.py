def tuple_to_dict(t):
    return {t[i]: t[i + 1] for i in range(0, len(t) - 1, 2)}