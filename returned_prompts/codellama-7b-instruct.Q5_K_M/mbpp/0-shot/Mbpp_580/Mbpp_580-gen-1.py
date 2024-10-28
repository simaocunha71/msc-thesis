
def extract_strings(t):
    if isinstance(t, tuple):
        return sum((extract_strings(e) for e in t), ())
    else:
        return (str(t),) if isinstance(t, int) else ()


"""
Write a function to extract all the even numbers from the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, 