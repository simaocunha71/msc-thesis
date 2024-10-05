```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isEqualToSumEven(int n) {
        if (n < 8) {
            return false;
        }
        if (n % 2 != 0) {
            return false;
        }
        int half = n / 2;
        if (half % 2 != 0) {
            return false;
        }
        int quarter = half / 2;
        return quarter % 2 == 0;
    }
}
```