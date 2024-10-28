    def sort_even(l: list):
        sorted_even = sorted(l[i] for i in range(0, len(l), 2))
        return l[:len(l)//2:2] + sorted_even + l[1::2]


