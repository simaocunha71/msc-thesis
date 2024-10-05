Here is the implementation in Java:

```java
import java.util.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        List<Integer> result = new ArrayList<>();
        if (n < 2) {
            return result;
        }
        result.add(2);
        for (int i = 3; i < n; i += 2) {
            if (isPrime(i)) {
                result.add(i);
            }
        }
        return result;
    }

    public boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

The function `countUpTo` iterates over the numbers from 3 to `n-1` in steps of 2 (since all primes are of the form 6k ± 1), and checks if each number is prime using the `isPrime` function. If a number is prime, it is added to the result list. The function returns the list of prime numbers.

The `isPrime` function checks if a number is prime by iterating over the numbers from 2 to the square root of the number, and checking if the number is divisible by any of these numbers. If it is, it is not prime. If it is not divisible by any of these numbers, it is prime. The function returns `true` if the number is prime, and `false` otherwise. 