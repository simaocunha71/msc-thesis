```java
import java.util.*;
import java.lang.*;

class Solution {
    public int primeFib(int n) {
        // Initialize the first two Fibonacci numbers
        int a = 1;
        int b = 1;
        // Initialize the counter for prime Fibonacci numbers
        int count = 0;
        // Loop until we find the nth prime Fibonacci number
        while (count < n) {
            // Calculate the next Fibonacci number
            int next = a + b;
            // Check if the next Fibonacci number is prime
            if (isPrime(next)) {
                count++;
                // If it is, check if it's the nth prime Fibonacci number
                if (count == n) {
                    return next;
                }
            }
            // Update the Fibonacci numbers
            a = b;
            b = next;
        }
        // If we haven't found the nth prime Fibonacci number, return -1
        return -1;
    }

    // Helper function to check if a number is prime
    private boolean isPrime(int num) {
        // Check if the number is less than 2
        if (num < 2) {
            return false;
        }
        // Check if the number is divisible by any number from 2 to the square root of the number
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        // If the number is not divisible by any number from 2 to the square root of the number, it is prime
        return true;
    }
}
```