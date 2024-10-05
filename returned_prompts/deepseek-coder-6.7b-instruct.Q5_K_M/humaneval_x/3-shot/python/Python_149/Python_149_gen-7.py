    def key_func(s):
        return len(s), s

    return sorted(filter(lambda x: len(x) % 2 == 0, lst), key=key_func)


