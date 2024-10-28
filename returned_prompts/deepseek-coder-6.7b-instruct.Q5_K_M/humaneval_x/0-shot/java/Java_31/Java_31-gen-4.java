        if (n == 2 || n == 3) return true;
        if (n <= 1 || n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2)
            if (n % i == 0)
                return false;
        return true;
    }
}

Explanation:

The function isPrime() checks if a given integer is prime. 

It first handles special cases:
- if the number is 2 or 3, it returns true, as they are the first two prime numbers.
- if the number is less than or equal to 1 or if it is even (except 2), it returns false, because these numbers can't be prime.

Then it enters the loop to check divisors. It starts from 3 and goes up to the square root of the number. If the number is divisible by any of these, it returns false. If no divisor is found, the number is prime and the function returns true.

The reason why we only check up to the square root of n is because a larger factor of n would be a multiple of smaller factor that has already been checked.

The step of 2 in the loop is used to skip even numbers, since they can't be prime (except 2).

This method is known as the Sieve of Eratosthenes, which is an ancient algorithm for finding all prime numbers up to any given limit. It does so by iteratively marking the multiples of each prime number starting from 2. The multiples of a given prime are generated as a sequence of numbers starting from that prime, with a constant difference between them that is equal to that prime. This is the key distinction between this method and any other primality test: the test divides the input number by each prime less than the square root of the input number, rather than testing divisibility by all numbers up to the input number.

This method is efficient, but it is not the only efficient method for finding primes, and it is not the only primality test that can be used, depending on the specific requirements of the problem.
*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.