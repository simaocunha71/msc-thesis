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
        // Initialize an array to store the prime factors
        int[] primeFactors = new int[3];
        int index = 0;

        // Find the prime factors of the given number
        for (int i = 2; i <= a; i++) {
            while (a % i == 0) {
                primeFactors[index++] = i;
                a /= i;
                if (index > 3) {
                    // More than 3 prime factors, return false
                    return false;
                }
            }
        }

        // Check if there are exactly 3 prime factors
        if (index == 3) {
            // Check if all prime factors are different
            return primeFactors[0] != primeFactors[1] && primeFactors[1] != primeFactors[2] && primeFactors[0] != primeFactors[2];
        } else {
            // Less or more than 3 prime factors, return false
            return false;
        }
    }
}
```