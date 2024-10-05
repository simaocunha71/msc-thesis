```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fib4(int n) {
        int[] fib = new int[n + 1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 2;
        fib[3] = 0;
        for (int i = 4; i <= n; i++) {
            fib[i] = fib[i - 1] + fib[i - 2] + fib[i - 3] + fib[i - 4];
        }
        return fib[n];
    }
}
```