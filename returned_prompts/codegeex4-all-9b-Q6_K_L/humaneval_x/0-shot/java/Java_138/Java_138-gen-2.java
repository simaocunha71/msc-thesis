```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isEqualToSumEven(int n) {
        if (n < 8) {
            return false;
        }
        for (int i = 2; i <= n; i += 2) {
            if (n - i >= 6 && (n - i) % 2 == 0) {
                return true;
            }
        }
        return false;
    }
}
```