```java
import java.util.*;
import java.lang.*;

class Solution {
    public String intersection(List<Integer> interval1, List<Integer> interval2) {
        if (interval1.get(1) < interval2.get(0) || interval2.get(1) < interval1.get(0)) {
            return "NO";
        }

        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));

        if (isPrime(end - start + 1)) {
            return "YES";
        } else {
            return "NO";
        }
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
