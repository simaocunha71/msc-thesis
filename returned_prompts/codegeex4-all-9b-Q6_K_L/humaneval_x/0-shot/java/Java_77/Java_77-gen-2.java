```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean iscube(int a) {
        if (a == 0) return true;
        int root = (int) Math.round(Math.cbrt(a));
        return root * root * root == a;
    }
}
```