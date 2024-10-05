```java
import java.util.*;
import java.lang.*;

class Solution {
    public long specialFactorial(int n) {
        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= factorial(i);
        }
        return result;
    }

    private long factorial(int num) {
        long result = 1;
        for (int i = 1; i <= num; i++) {
            result *= i;
        }
        return result;
    }
}
```