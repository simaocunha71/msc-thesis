```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean anyInt(Object x, Object y, Object z) {
        int a = (int) x;
        int b = (int) y;
        int c = (int) z;
        return (a == b + c || b == a + c || c == a + b);
    }
}
```