    def get_max_triples(n):
        res = 0
        for i in range(1, n + 1):
            if (i * i - i + 1) % 3 == 0:
                res += 1
        return res


