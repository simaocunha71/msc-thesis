    def sort_even(l: list):
        l_even = l[::2]
        sorted_even = sorted(l_even)
        return l[:len(l)//2:2] + sorted_even + l[1::2]


