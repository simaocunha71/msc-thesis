```java
import java.util.*;
import java.lang.*;

class Solution {
    public int startsOneEnds(int n) {
        int result = 0;
        if (n == 1) {
            return 1;
        }
        result += 9 * (int) Math.pow(9, n - 2);
        result += (int) Math.pow(9, n - 1);
        return result;
    }
}
```