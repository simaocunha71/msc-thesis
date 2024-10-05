        if (n <= 1) {
            return false;
        }
        if (n <= 3) {
            return true;
        }

        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }

        for (int i = 5; i * i <= n; i = i + 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }

        return true;
    }
}

The code works by first checking if the number is less than or equal to 1, in which case it is not prime. Then it checks if the number is less than or equal to 3, in which case it is prime. If the number is divisible by 2 or 3, it is not prime.

After these initial checks, the code then enters a loop where it checks if the number is divisible by any number up to the square root of the number. If the number is divisible by any of these numbers, it is not prime. If the number is not divisible by any of these numbers, it is prime. This is based on the fact that a larger factor of the number must be a multiple of a smaller factor that has already been checked.

The loop starts with 5 and increments by 6 in each iteration. This is because all prime numbers are of the form 6k ± 1, k ∈ N. This means that all primes are of the form 6k-1 or 6k+1, for some k. By checking for divisibility by 2 and 3 first, we can eliminate many numbers in this loop.

Finally, if none of the above conditions are met, the number is prime, so the function returns true.

This function is efficient because it only needs to check divisibility up to the square root of the number.
    """

print(Solution().isPrime(6)) # False
print(Solution().isPrime(101)) # True
print(Solution().isPrime(11)) # True
print(Solution().isPrime(13441)) # False
print(Solution().isPrime(61)) # True
