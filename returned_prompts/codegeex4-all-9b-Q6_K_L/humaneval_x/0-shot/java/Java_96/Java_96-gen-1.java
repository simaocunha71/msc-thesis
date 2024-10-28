Here is a Java solution using a helper function to check if a number is prime, and an ArrayList to store the prime numbers:

```java
import java.util.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        ArrayList<Integer> primes = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }
        return primes;
    }
    
    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

This solution iterates from 2 to n-1, checking if each number is prime using the `isPrime` helper function. If a number is prime, it is added to the ArrayList. The ArrayList is then returned as the result.