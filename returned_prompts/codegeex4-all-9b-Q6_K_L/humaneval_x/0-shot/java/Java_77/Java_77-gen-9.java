```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean iscube(int a) {
        if (a < 0) {
            a = -a;
        }
        int sqrt = (int) Math.sqrt(a);
        return sqrt * sqrt == a;
    }
}
```