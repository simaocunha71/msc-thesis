```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSimplePower(int x, int n) {
        if (x == 1) {
            return true;
        }
        int power = 1;
        while (power <= x) {
            if (power == x) {
                return true;
            }
            power *= n;
        }
        return false;
    }
}
```