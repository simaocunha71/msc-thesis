```java
import java.util.*;
import java.lang.*;

class Solution {
    public int primeFib(int n) {
        int count = 0;
        int fib1 = 0;
        int fib2 = 1;
        int fib = fib1 + fib2;

        while (count < n) {
            fib1 = fib2;
            fib2 = fib;
            fib = fib1 + fib2;

            if (isPrime(fib)) {
                count++;
            }
        }

        return fib;
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