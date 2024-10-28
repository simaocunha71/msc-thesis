```java
import java.util.*;
import java.lang.*;

class Solution {
    public int sumToN(int n) {
        if (n == 0) {
            return 0;
        } else {
            return n + sumToN(n - 1);
        }
    }
}
```