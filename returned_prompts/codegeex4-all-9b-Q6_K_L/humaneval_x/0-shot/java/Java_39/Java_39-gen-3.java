```java
import java.util.*;
import java.lang.*;

class Solution {
    public int primeFib(int n) {
        int a = 0, b = 1;
        int count = 0;
        while (count < n) {
            int c = a + b;
            a = b;
            b = c;
            if (isPrime(c)) {
                count++;
            }
        }
        return b;
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
