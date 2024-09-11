def count_first_elements(tup):
    return sum(1 for x in tup if isinstance(x, tuple) or x in tup[:tup.index(x)])