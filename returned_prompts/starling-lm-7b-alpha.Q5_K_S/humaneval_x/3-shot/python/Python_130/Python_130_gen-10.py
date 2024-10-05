    def tri_recur(n):
        if n == 0:
            return []
        if n == 1:
            return [1]
        if n == 2:
            return [1, 3]
        if n % 2 == 0:
            return [1, 3] + tri_recur(n // 2)
        else:
            return [1] + tri_recur(n - 1) + tri_recur(n - 2) + tri_recur(n + 1)
    return tri_recur(n)


