    def key_func(s):
        return (len(s), s)

    return sorted(filter(lambda s: len(s) % 2 == 0, lst), key=key_func)


