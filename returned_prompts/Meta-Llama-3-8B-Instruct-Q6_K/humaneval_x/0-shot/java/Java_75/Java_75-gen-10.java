        for(int i = 2; i < a; i++) {
            if (isPrime(i)) {
                for(int j = i; j < a; j++) {
                    if (isPrime(j)) {
                        int k = a / (i * j);
                        if (isPrime(k)) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for(int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
SOLUTION:
This solution is a brute force approach. It checks every possible combination of 3 numbers to see if they are prime. The isPrime function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If the number is divisible, it is not prime. If it is not divisible, it is prime.

The isMultiplyPrime function checks every possible combination of 3 numbers to see if they are prime. It does this by first checking if the first number is prime, then checking every possible combination of numbers that are less than the given number and greater than or equal to the first number. It does this by iterating over the range of numbers from the first number to the given number, and for each number, it checks if the number is prime. If it is, it calculates the third number by dividing the given number by the product of the first two numbers, and checks if this number is also prime. If it is, it returns true. If it does not find a combination of 3 prime numbers, it returns false.

This solution has a time complexity of O(n^2), where n is the given number, because it checks every possible combination of 3 numbers. This is not very efficient, but it is a simple and easy to understand solution. A more efficient solution would be to use a sieve to generate all prime numbers up to the given number, and then check if the given number is the product of 3 prime numbers. This would have a time complexity of O(n), which is much faster for large inputs.