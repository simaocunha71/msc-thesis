```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean rightAngleTriangle(int a, int b, int c) {
        if (a <= 0 || b <= 0 || c <= 0) {
            return false;
        }
        if (a == b || b == c || a == c) {
            return false;
        }
        return Math.pow(a, 2) + Math.pow(b, 2) == Math.pow(c, 2);
    }
}
```