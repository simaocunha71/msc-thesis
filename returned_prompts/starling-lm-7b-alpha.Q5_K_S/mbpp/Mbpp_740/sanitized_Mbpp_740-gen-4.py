def tuple_to_dict(t):
    assert type(t) == tuple
    assert len(t) % 2 == 0
    assert all(type(i) == int for i in t)
    return {t[i]: t[i+1] for i in range(0, len(t), 2)}