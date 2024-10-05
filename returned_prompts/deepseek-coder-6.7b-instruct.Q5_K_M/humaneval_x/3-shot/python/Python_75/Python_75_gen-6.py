    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    factors = [i for i in range(2, a) if a % i == 0 and is_prime(i)]
    return len(factors) == 3 and a == factors[0]*factors[1]*factors[2]


