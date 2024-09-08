def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
            while result % 10 == 0:
                result /= 10
            result = int(result % 100000)
        return result % 10