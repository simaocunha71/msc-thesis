```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSimplePower(int x, int n) {
        if (x == 1) return true;
        if (n == 1) return false;
        if (x == n) return true;
        if (x % n != 0) return false;
        int power = n;
        while (power < x) {
            power *= n;
        }
        return power == x;
    }
}
```