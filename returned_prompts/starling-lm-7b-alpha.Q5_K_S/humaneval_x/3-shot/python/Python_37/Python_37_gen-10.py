    def sort_even(l: list):
        l_copy = l.copy()
        for i in range(0, len(l_copy), 2):
            l_copy[i] = l[i]
        l_copy.sort()
        return l_copy


