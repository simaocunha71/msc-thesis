    def f(n: int) -> List[int]:
        result = []
        for i in range(1, n + 1):
            if i % 2 == 0:
                result.append(fact(i))
            else:
                result.append(sum(range(1, i + 1)))

        return result

    def fact(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * fact(n - 1)

    return f


