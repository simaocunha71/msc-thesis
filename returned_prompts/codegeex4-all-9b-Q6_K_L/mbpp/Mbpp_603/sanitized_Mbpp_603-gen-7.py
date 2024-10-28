def get_ludic(n):
    def is_ludic(num):
        def prime_factors(num):
            i = 2
            factors = []
            while i * i <= num:
                if num % i:
                    i += 1
                else:
                    num //= i
                    factors.append(i)
            if num > 1:
                factors.append(num)
            return factors

        factors = prime_factors(num)
        return len(set(factors)) == 1

    return [i for i in range(1, n + 1) if is_ludic(i)]