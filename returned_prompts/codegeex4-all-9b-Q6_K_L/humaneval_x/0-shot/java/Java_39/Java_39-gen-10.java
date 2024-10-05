```java
import java.util.*;
import java.lang.*;

class Solution {
    public int primeFib(int n) {
        // Generate all Fibonacci numbers and check if they are prime
        List<Integer> fibPrimes = new ArrayList<>();
        int a = 0, b = 1;
        while (fibPrimes.size() < n) {
            int c = a + b;
            a = b;
            b = c;
            if (isPrime(c)) {
                fibPrimes.add(c);
            }
        }
        return fibPrimes.get(n - 1);
    }

    private boolean isPrime(int num) {
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
}
```

Explanation:
1. The `primeFib` function takes an integer `n` as input and returns the `n`-th Fibonacci number that is also prime.
2. We initialize two variables `a` and `b` to 0 and 1 respectively, which represent the first two Fibonacci numbers.
3. We use a while loop to generate Fibonacci numbers until we find `n` prime Fibonacci numbers.
4. Inside the loop, we calculate the next Fibonacci number `c` as the sum of `a` and `b`.
5. We update `a` and `b` to the next two Fibonacci numbers.
6. We check if `c` is prime using the `isPrime` function.
7. If `c` is prime, we add it to the `fibPrimes` list.
8. Once we have found `n` prime Fibonacci numbers, we return the `n`-th number from the `fibPrimes` list.
9. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if it is divisible by any number in that range.
10. If the number is divisible by any number in that range, it is not prime and the function returns `false`. Otherwise, it returns `true`.