```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        if (n <= 1) {
            return new ArrayList<>();
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                result.add(i);
            }
        }
        return result;
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