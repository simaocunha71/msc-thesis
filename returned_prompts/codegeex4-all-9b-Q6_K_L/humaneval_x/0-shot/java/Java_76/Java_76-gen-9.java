Here is a Java solution. This solution uses a while loop to check if x is a simple power of n. The loop continues until x is less than or equal to n. If x is equal to 1, then it is a simple power of n, so it returns true. Otherwise, it divides x by n and checks if the remainder is 0. If the remainder is not 0, then x is not a simple power of n, so it returns false.
```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSimplePower(int x, int n) {
        while (x > n) {
            x /= n;
        }
        return x == 1;
    }
}
```