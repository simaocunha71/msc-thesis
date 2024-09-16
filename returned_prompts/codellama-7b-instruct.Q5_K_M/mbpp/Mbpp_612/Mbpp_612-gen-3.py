def merge(lst):
    return [list(map(lambda *x: x, *zip(*lst)))
