```java
import java.util.*;
import java.lang.*;

class Solution {
    public int startsOneEnds(int n) {
        if (n <= 1) {
            return 1;
        }
        if (n == 2) {
            return 9;
        }
        int count = 9;
        for (int i = 2; i < n; i++) {
            count *= 9;
        }
        return count * 2;
    }
}
```