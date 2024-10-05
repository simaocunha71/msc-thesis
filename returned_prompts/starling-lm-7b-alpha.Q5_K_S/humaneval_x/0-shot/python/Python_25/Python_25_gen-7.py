    def factorize(n):
        """ Return list of prime factors of given integer in the order from smallest to largest.
        Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
        Input number should be equal to the product of all factors
        """
        # base case
        if n == 1:
            return [1]
        # if number is prime, return number itself
        if n == 2 or n == 3 or n == 5 or n == 7:
            return [n]
        # check divisibility by 2
        if n % 2 == 0:
            return [2] + factorize(n // 2)
        # check divisibility by 3
        if n % 3 == 0:
            return [3] + factorize(n // 3)
        # check divisibility by 5
        if n % 5 == 0:
            return [5] + factorize(n // 5)
        # check divisibility by 7
        if n % 7 == 0:
            return [7] + factorize(n // 7)
        # if none of the above, use binary search
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return [i] + factorize(n // i)
        return [n]

    return factorize(n)


# Run tests
print(factorize(8) == [2, 2, 2])
print(factorize(25) == [5, 5])
print(factorize(70) == [2, 5, 7])














































































































