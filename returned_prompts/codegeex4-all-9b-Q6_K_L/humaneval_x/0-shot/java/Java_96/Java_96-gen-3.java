```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        List<Integer> primes = new ArrayList<>();
        if (n <= 1) {
            return primes;
        }
        primes.add(2);
        for (int i = 3; i < n; i += 2) {
            if (isPrime(i, primes)) {
                primes.add(i);
            }
        }
        return primes;
    }

    private boolean isPrime(int num, List<Integer> primes) {
        for (int prime : primes) {
            if (num % prime == 0) {
                return false;
            }
            if (prime * prime > num) {
                break;
            }
        }
        return true;
    }
}
```