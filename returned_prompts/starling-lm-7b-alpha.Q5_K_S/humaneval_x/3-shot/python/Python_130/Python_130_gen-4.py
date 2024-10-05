    def tribonacci(n):
        res = [0] * (n + 1)
        res[1] = 3
        if n % 2 == 0:
            for i in range(2, n + 1):
                res[i] = 1 + i / 2
        else:
            res[2] = 1
            res[3] = 3
            for i in range(4, n + 1):
                res[i] = res[i - 1] + res[i - 2] + res[i + 1]
        return res


