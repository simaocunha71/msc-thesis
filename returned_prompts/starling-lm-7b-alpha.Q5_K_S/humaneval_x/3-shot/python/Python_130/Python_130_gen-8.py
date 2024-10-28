    def tribonacci(n):
        if n == 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1, 3]
        else:
            result = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n+1)
        return result

    return tribonacci(n)


