```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100.
    Example:
    isMultiplyPrime(30) == true
    30 = 2 * 3 * 5
     */
    public boolean isMultiplyPrime(int a) {
        // Check if the number is less than 2, 2 is the smallest prime number
        if (a < 2) {
            return false;
        }

        // Count the number of prime factors
        int count = 0;
        for (int i = 2; i <= a; i++) {
            // Check if i is a prime number
            if (isPrime(i)) {
                // Check if a is divisible by i
                while (a % i == 0) {
                    count++;
                    a /= i;
                    // If the count is greater than 3, it is not a multiplication of 3 prime numbers
                    if (count > 3) {
                        return false;
                    }
                }
            }
        }

        // If the count is equal to 3, it is a multiplication of 3 prime numbers
        return count == 3;
    }

    // Function to check if a number is prime
    public boolean isPrime(int n) {
        // Check if n is less than 2, 2 is the smallest prime number
        if (n < 2) {
            return false;
        }

        // Check if n is divisible by any number from 2 to n-1
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        // If n is not divisible by any number from 2 to n-1, it is a prime number
        return true;
    }
}
```

This code checks if a given number is a multiplication of 3 prime numbers. It uses a helper function `isPrime` to check if a number is prime or not. The `isMultiplyPrime` function iterates through the numbers from 2 to the given number and checks if each number is prime. If a prime number is found, it checks if the given number is divisible by that prime number. If the given number is divisible by the prime number, it