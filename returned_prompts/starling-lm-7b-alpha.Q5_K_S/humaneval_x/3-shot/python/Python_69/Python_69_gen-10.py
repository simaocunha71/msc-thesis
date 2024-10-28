    def frequency(n):
        return lst.count(n)

    def search(lst):
        for n in reversed(sorted(lst)):
            if frequency(n) >= n:
                return n
        return -1


