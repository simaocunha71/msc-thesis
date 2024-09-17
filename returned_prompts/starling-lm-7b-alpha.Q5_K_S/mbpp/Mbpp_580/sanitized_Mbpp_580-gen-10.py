def extract_even(tup):
    even_tuple = []
    while tup:
        item = tup.pop()
        if isinstance(item, tuple):
            tup = item + tup
            continue
        if item % 2 == 0:
            even_tuple.append(item)
    return even_tuple