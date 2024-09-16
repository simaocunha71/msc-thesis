
def extract_even(nested_tuple):
    return tuple(
        t
        for t in nested_tuple
        if isinstance(t, tuple)
        else t
            if t % 2 == 0
            else None
    )
