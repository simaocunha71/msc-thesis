    def tri(n):
        if n == 0:
            return []
        if n == 1:
            return [1]
        if n == 2:
            return [3, 1]
        if n % 2 == 0:
            result = tri(n - 2)
        else:
            result = tri(n - 1) + tri(n - 2) + tri(n + 1)
        result.insert(0, 1 + n / 2)
        return result


