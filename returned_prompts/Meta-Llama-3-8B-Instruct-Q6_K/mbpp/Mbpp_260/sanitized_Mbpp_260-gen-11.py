def newman_prime(n):
    def is_nsw_prime(num):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    while True:
        if is_nsw_prime(num):
            if count == n:
                return num
            count += 1
        num += 1