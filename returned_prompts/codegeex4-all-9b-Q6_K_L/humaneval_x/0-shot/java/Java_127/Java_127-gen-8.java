```java
import java.util.*;
import java.lang.*;

class Solution {
    public String intersection(List<Integer> interval1, List<Integer> interval2) {
        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));
        if (start > end) {
            return "NO";
        }
        int length = end - start + 1;
        return isPrime(length) ? "YES" : "NO";
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```