    def tri(n):
        seq = [3]
        if n == 0:
            return seq
        elif n == 1:
            return seq + [1]
        elif n == 2:
            return seq + [1, 2]
        elif n % 2 == 0:
            for _ in range(3, n + 1):
                seq.append(1 + _ / 2)
            return seq
        else:
            for _ in range(3, n + 1):
                seq.append(tri(_ - 1) + tri(_ - 2) + tri(_ + 1))
            return seq

    return tri(n)


