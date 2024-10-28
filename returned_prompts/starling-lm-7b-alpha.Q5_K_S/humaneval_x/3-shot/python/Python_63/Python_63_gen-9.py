    def fibfib(n):
        fibs = [0, 0, 1]
        while len(fibs) < n + 1:
            fibs.append(fibs[-1] + fibs[-2] + fibs[-3])
        return fibs[n]


