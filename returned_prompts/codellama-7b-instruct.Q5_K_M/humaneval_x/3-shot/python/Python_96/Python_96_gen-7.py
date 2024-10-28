    if n == 0 or n < 0:
        return []
    else:
        primes = [2]
        for i in range(3, n+1, 2):
            for j in range(2, int(i ** 0.5)+1):
                if i % j == 0:
                    break
            else:
                primes.append(i)

        return primes


