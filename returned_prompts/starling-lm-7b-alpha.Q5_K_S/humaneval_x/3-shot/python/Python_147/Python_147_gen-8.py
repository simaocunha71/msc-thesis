    def solve(n):
        result = 0
        for i in range(1, n+1):
            v = i * i - i + 1
            if v % 3 == 0:
                result += 1
        return result

    return solve(n)


