def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def sum_divisors(n):
        result = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i * i == n:
                    result += i
                else:
                    result += i + n // i
        return result
    return sum_divisors(gcd(a, b))//2