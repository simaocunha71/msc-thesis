
    def search(lst):
        dct = {}
        for i in lst:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1
        for i in dct:
            if dct[i] >= i:
                return i
        return -1
