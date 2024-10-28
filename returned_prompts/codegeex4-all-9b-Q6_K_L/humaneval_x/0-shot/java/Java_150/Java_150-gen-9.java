```java
import java.util.*;
import java.lang.*;

class Solution {
    public int xOrY(int n, int x, int y) {
        if (n == 2) {
            return x;
        }
        if (n <= 1 || n % 2 == 0) {
            return y;
        }
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                return y;
            }
        }
        return x;
    }
}
```