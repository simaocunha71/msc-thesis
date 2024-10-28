Here is the Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    private static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public String intersection(List<Integer> interval1, List<Integer> interval2) {
        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));

        if (start > end) {
            return "NO";
        }

        int length = end - start + 1;
        return isPrime(length) ? "YES" : "NO";
    }
}
```

This solution works by first finding the start and end of the intersection of the two intervals. If the start is greater than the end, the intervals don't intersect, so we return "NO".

If the intervals do intersect, we calculate the length of the intersection and check if it's a prime number using the `isPrime` method. If it is, we return "YES", otherwise we return "NO".