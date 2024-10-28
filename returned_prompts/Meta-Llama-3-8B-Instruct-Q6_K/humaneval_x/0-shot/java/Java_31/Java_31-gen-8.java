        if (n <= 1) {
            return false;
        }
        if (n <= 3) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        int i = 5;
        while (i * i <= n) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
            i = i + 6;
        }
        return true;
    }
}

Explanation:

This solution checks whether a given number is prime or not. It uses the following strategy:

1.  If the number is less than or equal to 1, it is not prime, so return false.
2.  If the number is less than or equal to 3, it is prime, so return true.
3.  If the number is divisible by 2 or 3, it is not prime, so return false.
4.  Otherwise, check if the number is divisible by any odd number up to the square root of the number. If it is, it is not prime, so return false.
5.  If the number is not divisible by any of these numbers, it is prime, so return true.

This solution is efficient because it only checks divisibility up to the square root of the number, which reduces the number of checks needed. It also uses a simple and efficient algorithm for checking divisibility, which is to check if the number is divisible by any odd number up to the square root of the number.

The unit tests provided in the problem statement demonstrate the correct behavior of the `isPrime` function. For example, `isPrime(6)` returns `false` because 6 is not a prime number, and `isPrime(101)` returns `true` because 101 is a prime number. Similarly, `isPrime(11)` returns `true` because 11 is a prime number, and `isPrime(4)` returns `false` because 4 is not a prime number. The other unit tests also demonstrate the correct behavior of the `isPrime` function.