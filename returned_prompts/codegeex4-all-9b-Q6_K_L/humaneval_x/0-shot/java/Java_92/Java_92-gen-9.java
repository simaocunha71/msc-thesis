```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean anyInt(Object x, Object y, Object z) {
        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) {
            return false;
        }
        int a = (Integer) x;
        int b = (Integer) y;
        int c = (Integer) z;
        return (a == b + c || b == a + c || c == a + b);
    }
}
```