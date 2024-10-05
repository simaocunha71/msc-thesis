    def is_prime(n: int) -> bool:
        """ Check if number is prime.
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_largest_prime(nums: List[int]) -> int:
        """ Given a list of numbers, return the largest prime number from the list.
        >>> get_largest_prime([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3])
        181
        >>> get_largest_prime([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1])
        181
        >>> get_largest_prime([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3])
        83278
        """
        return max(filter(is_prime, nums))

    def get_sum_of_digits(number: int) -> int:
        """ Given a number, return the sum of its digits.
        >>> get_sum_of_digits(356)
        15
        >>> get_sum_of_digits(241)
        8
        >>> get_sum_of_digits(1233)
        13
        """
        return sum(map