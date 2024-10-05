    def brazilian_factorial(n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

    def special_factorial(n):
        result = 1
        for i in range(1, n+1):
            result *= brazilian_factorial(i)
        return result

    return special_factorial(n)  # This will be the final function


