    def tribonacci(n):
        if n==1:
            return [3]
        if n==2:
            return [3,1]
        if n==3:
            return [3,1,2]
        else:
            result = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n+1)
            result.insert(0, 1)
            return result
    return tribonacci(n)


