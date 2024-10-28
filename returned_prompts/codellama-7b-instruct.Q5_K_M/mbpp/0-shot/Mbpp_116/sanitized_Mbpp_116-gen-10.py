def tuple_to_int(t):
    assert all(i>0 for i in t)
    return sum(i*10**(len(t)-1-i) for i in t)