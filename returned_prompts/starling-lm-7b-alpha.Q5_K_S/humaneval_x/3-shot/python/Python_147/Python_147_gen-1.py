    def get_max_triples(n):
        result = 0
        for i in range(1, n + 1):
            if (i * i - i + 1) % 3 == 0:
                result += 1
        return result // 3


