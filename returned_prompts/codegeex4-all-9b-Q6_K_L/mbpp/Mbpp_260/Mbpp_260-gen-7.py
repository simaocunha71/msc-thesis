def newman_prime(n):
    newman = 2
    count = 0
    while True:
        for i in range(2, int(newman ** 0.5) + 1):
            if newman % i == 0:
                break
        else:
            count += 1
        if count == n:
            return newman
        newman += 1

