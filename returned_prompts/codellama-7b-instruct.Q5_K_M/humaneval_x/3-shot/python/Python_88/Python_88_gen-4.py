    if not array:
        return array

    def sort_fn(a, b):
        if (a + b) % 2 == 0:
            return b - a
        return a - b

    return sorted(array, key=sort_fn)


