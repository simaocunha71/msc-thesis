```java
import java.util.*;
import java.lang.*;

class Solution {
    public int chooseNum(int x, int y) {
        if (y < x) {
            return -1;
        }
        if ((x % 2 == 0) && (y % 2 == 0)) {
            return Math.max(x, y);
        }
        if (x % 2 == 0) {
            return x;
        }
        if (y % 2 == 0) {
            return y;
        }
        if (x < y) {
            return x + 1;
        }
        return y + 1;
    }
}
```