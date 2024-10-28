
def extract_even(tup):
    def flatten(tup):
        for elem in tup:
            if isinstance(elem, tuple):
                flatten(elem)
            else:
                yield elem
    return tuple(filter(lambda x: x % 2 == 0, flatten(tup)))


