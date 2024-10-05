    def key_func(s):
        return len(s), s

    return sorted([s for s in lst if len(s) % 2 == 0], key=key_func)


