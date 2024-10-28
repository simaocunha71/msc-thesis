Here is the solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int primeFib(int n) {
        int a = 0, b = 1;
        int fib = 0;
        int count = 0;
        while(count < n) {
            fib = a + b;
            a = b;
            b = fib;
            if (isPrime(fib)) {
                count++;
            }
        }
        return fib;
    }

    private boolean isPrime(int num) {
        if(num <= 1) {
            return false;
        }
        for(int i = 2; i <= Math.sqrt(num); i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

The `primeFib` function generates Fibonacci numbers and checks if they are prime. If a prime Fibonacci number is found, the count is incremented. When the count reaches the input value `n`, the function returns the current Fibonacci number.

The `isPrime` function checks if a number is prime by checking if it is divisible by any number from 2 to its square root. If it is divisible by any number, it is not prime. If it is not divisible by any number, it is prime.