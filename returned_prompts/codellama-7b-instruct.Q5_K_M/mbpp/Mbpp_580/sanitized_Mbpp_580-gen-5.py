def extract_even(tup):
    if len(tup) == 0:
        return tup
    else:
        if isinstance(tup[0], tuple):
            return (extract_even(tup[0]),) + extract_even(tup[1:])
        else:
            if len(tup) % 2 == 0:
                return (tup[0],) + extract_even(tup[1:])
            else:
                return extract_even(tup[1:])