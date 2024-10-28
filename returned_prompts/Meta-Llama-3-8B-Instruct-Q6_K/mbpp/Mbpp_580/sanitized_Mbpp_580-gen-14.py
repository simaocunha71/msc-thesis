def extract_even(t):
    new_t = []
    for i in t:
        if isinstance(i, tuple):
            new_t.append(extract_even(i))
        elif i % 2 == 0:
            new_t.append(i)
    return tuple(new_t)