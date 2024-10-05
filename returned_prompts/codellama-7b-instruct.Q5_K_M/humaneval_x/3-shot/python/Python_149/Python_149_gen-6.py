    def _sort(a, b):
        if len(a) != len(b):
            return len(a) - len(b)
        return a < b

    return sorted(lst, key=lambda x: (len(x), x), reverse=True)


