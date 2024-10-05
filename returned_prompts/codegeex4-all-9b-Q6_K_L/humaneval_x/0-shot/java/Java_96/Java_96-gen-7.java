```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        if (n <= 1) {
            return new ArrayList<Integer>();
        }

        List<Integer> primes = new ArrayList<Integer>();
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);

        for (int i = 2; i * i < n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        for (int i = 2; i < n; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }

        return primes;
    }
}
```