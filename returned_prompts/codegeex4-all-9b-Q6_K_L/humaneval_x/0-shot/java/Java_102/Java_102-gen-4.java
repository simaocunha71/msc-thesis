```java
import java.util.*;
import java.lang.*;

class Solution {
    public int chooseNum(int x, int y) {
        int res = -1;
        if (x > y) return res;
        for (int i = x; i <= y; i++) {
            if (i % 2 == 0) {
                res = i;
                break;
            }
        }
        return res;
    }
}
```
This solution iterates from `x` to `y` and checks if each number is even. If it finds an even number, it breaks the loop and returns it. If it doesn't find any even number, it returns `-1`. The time complexity of this solution is O(n), where n is the difference between `y` and `x`.