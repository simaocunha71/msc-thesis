def newman_prime(n):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
        if count == n:
            return num
        num += 1

print(newman_prime(3))  # 7
"""

