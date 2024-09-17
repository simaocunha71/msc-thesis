
def newman_prime(n):
    count = 0
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            if count == n:
                return num
        num += 1


