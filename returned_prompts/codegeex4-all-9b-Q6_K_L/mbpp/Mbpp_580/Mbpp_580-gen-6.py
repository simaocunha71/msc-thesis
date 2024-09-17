def extract_even(test_tuple):
    res = []
    for i in test_tuple:
        if isinstance(i, tuple):
            res.append(extract_even(i))
        elif i % 2 == 0:
            res.append(i)
    return tuple(res)

