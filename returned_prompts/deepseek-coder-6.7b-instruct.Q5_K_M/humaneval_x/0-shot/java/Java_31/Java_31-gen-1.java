        if(n <= 1) {
            return false;
        }
        if(n <= 3) {
            return true;
        }
        if(n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        for(int i = 5; i * i <= n; i = i + 6) {
            if(n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

The code checks if a number is divisible by 2 or 3. If it is, it is not a prime number. Then it checks if the number is divisible by any number in the form 6k ± 1, where k is a positive integer. If the number is divisible by such a number, it is not a prime number. If it is not divisible by any of these numbers, it is a prime number.

The reason we only need to check divisors up to sqrt(n) is that a larger factor of the number would be a multiple of smaller factor that has already been checked.

The loop starts from 5 and increments i by 6 each time, because all prime numbers are of the form 6k ± 1, where k is a positive integer.

The reason we start from 5 and increment by 6 each time is because all primes are of the form 6k ± 1, for some k. This is because all integers can be expressed as 6k ± 1 for some k.

The loop continues while i*i is less than or equal to n. This is because if n is not a prime, it can be factored into two factors a and b. If both a and b were greater than the square root of n, a*b would be greater than n. So at least one of those factors must be less than or equal to the square root of n, and to check if n is prime, we only need to test for factors less than or equal to the square root.

If the number is not divisible by any of these numbers, it is a prime number.
*/

//Complexity: O(sqrt(n)) - time complexity.
//Complexity: O(1