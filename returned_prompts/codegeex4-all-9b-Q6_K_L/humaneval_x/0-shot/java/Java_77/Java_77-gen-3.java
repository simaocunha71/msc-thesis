```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean iscube(int a) {
        if (a == 0) {
            return true;
        }
        int b = (int) Math.round(Math.cbrt(a));
        return b * b * b == a;
    }
}
```