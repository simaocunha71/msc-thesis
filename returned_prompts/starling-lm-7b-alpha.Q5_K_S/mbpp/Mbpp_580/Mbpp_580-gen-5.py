
def extract_even(mixed_tup):
    new_tup = []
    for i in mixed_tup:
        if isinstance(i, tuple):
            new_tup.append(tuple(filter(lambda x: x % 2 == 0, i)))
        else:
            if i % 2 == 0:
                new_tup.append(i)
    return tuple(new_tup)


