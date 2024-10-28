    def tribonacci(n: int) -> List[int]:
        def _tribonacci(n: int) -> List[int]:
            if n == 0:
                return []

            if n == 1:
                return [1]

            if n == 2:
                return [1, 3]

            result = [1, 3]
            while len(result) < n + 1:
                result.append(result[-2] + result[-1] + result[-3])

            return result

        return _tribonacci(n)

    return tribonacci(n)


