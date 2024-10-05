    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    i = n - 1
    while i > 1:
        if is_prime(i):
            return i
        i -= 1
    return 1
# This function is not efficient for large inputs. It would be better to start from 2 and go up to the square root of n instead of going down from n. Also, you can use a more efficient algorithm to check for primality.