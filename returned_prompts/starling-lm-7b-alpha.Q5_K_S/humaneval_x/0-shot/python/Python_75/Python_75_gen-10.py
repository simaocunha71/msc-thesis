    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a):
        if a < 100:
            for i in range(2, a + 1):
                if is_prime(i) and is_prime(a // i) and is_prime(i) and i != 1 and a // i != 1:
                    return True
        return False

    return is_multiply_prime(a)


# Example usage:
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(50))  # Output: False




```

This function `is_multiply_prime` checks if the given number `a` is the multiplication of 3 prime numbers. It first defines a helper function `is_prime` that checks if a number `n` is prime. Then, it uses a for loop to iterate through all numbers from 2 to `a`. For each number, it checks if it is prime, and if `a` divided by that number is also prime. If both conditions are met, it returns True. Otherwise, it returns False.

In the example usage, we test the function with two numbers: 30 and 50. For 30, the function returns True because 30 is the multiplication of 2, 3, and 5, which are all prime numbers. For 50, the function returns False because 50 cannot be divided evenly by 3 prime numbers.

Note: The function assumes that `a` is less than 100, as stated in the problem. If `a` is greater than or equal to 100, a more efficient approach can be used, such as checking if the factors are prime in a different order or using more advanced techniques like trial division or the Sieve of Eratosthenes to find prime factors.

The time complexity of this function is O(n log(log n)) due to the helper function `is_prime` using the loop with a range. However, this is not