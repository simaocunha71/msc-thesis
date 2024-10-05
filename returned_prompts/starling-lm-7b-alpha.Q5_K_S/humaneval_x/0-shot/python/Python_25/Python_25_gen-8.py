    # Correct Solution:
    def factorize(n: int) -> List[int]:
        factors = []
        d = 2
        while n > 1:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        return factors

    # Alternative Solution:
    # def factorize(n: int) -> List[int]:
    #     """ Return list of prime factors of given integer in the order from smallest to largest.
    #     Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    #     Input number should be equal to the product of all factors
    #     """
    #     def prime_factors(n: int) -> List[int]:
    #         factors = []
    #         i = 2
    #         while n > 1:
    #             while n % i == 0:
    #                 factors.append(i)
    #                 n //= i
    #             i += 1
    #         return factors

    #     return prime_factors(n)

    return factorize


# Run tests
print(factorize(8) == [2, 2, 2])
print(factorize(25) == [5, 5])
print(factorize(70) == [2, 5, 7])


# More tests
print(factorize(6) == [2, 3])
print(factorize(10) == [2, 5])
print(factorize(1) == [1])
print(factorize(0) == [])
print(factorize(3) == [3])
print(factorize(13) == [13])
print(factorize(15) == [3, 5])
print(factorize(16) == [2, 2, 2, 2])
print(factorize(17) == [17])
print(factorize(18) == [2, 3, 3])
print(factorize(20) == [2, 2, 5])
print(