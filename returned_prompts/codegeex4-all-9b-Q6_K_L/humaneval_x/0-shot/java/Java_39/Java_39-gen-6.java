Here's the Java implementation for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int primeFib(int n) {
        int fib1 = 0;
        int fib2 = 1;
        int fib3;
        int count = 0;

        while (count < n) {
            fib3 = fib1 + fib2;
            if (isPrime(fib3)) {
                count++;
            }
            fib1 = fib2;
            fib2 = fib3;
        }
        return fib2;
    }

    public boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.primeFib(1)); // 2
        System.out.println(sol.primeFib(2)); // 3
        System.out.println(sol.primeFib(3)); // 5
        System.out.println(sol.primeFib(4)); // 13
        System.out.println(sol.primeFib(5)); // 89
    }
}
```

In this solution, `primeFib(int n)` calculates the n-th number that is both a Fibonacci number and a prime number. The helper function `isPrime(int num)` checks if a given number is prime. The main function `main(String[] args)` creates an instance of the Solution class and tests the `primeFib(int n)` function with different inputs.