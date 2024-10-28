```java
import java.util.*;
import java.lang.*;

class Solution {
    public String intersection(List<Integer> interval1, List<Integer> interval2) {
        int a = interval1.get(0);
        int b = interval1.get(1);
        int c = interval2.get(0);
        int d = interval2.get(1);
        int intersectStart = Math.max(a, c);
        int intersectEnd = Math.min(b, d);
        if (intersectStart > intersectEnd) {
            return "NO";
        }
        int intersectLength = intersectEnd - intersectStart + 1;
        return isPrime(intersectLength) ? "YES" : "NO";
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