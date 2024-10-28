def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def divisors(n):
        divisors = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        return divisors
    return sum(divisors(a) & divisors(b)) - a - b + gcd(a, b) if a != b else gcd(a, b)