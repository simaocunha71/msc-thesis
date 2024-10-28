    def f(n):
        ans = 0
        for i in range(1, n + 1):
            v = i * i - i + 1
            if v % 3 == 0:
                ans += 1
        return ans

    def g(n):
        ans = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                v = i * i - i + 1 + j * j - j + 1
                if v % 3 == 0:
                    ans += 1
        return ans

    def h(n):
        return g(n) - f(n) * f(n)

    return h(n)


