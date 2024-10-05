```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fib4(int n) {
        // initialize the first four elements of the fib4 sequence
        int a = 0;
        int b = 0;
        int c = 2;
        int d = 0;

        // compute the fib4 sequence iteratively
        for (int i = 4; i <= n; i++) {
            int temp = a + b + c + d;
            a = b;
            b = c;
            c = d;
            d = temp;
        }

        // return the n-th element of the fib4 sequence
        return d;
    }
}
```