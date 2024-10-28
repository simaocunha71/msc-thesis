```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        if (n < 2) {
            return new ArrayList<Integer>();
        }
        List<Integer> primes = new ArrayList<Integer>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }
        return primes;
    }

    private boolean isPrime(int num) {
        if (num < 2) {
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