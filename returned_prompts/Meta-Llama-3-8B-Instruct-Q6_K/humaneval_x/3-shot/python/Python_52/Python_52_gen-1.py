    return all(i < t for i in l)  # Python 3.x
    # return reduce(lambda x, y: x and y < t, l, True)  # Python 2.x


