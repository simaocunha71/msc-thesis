```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean anyInt(Object x, Object y, Object z) {
        return (int)x + (int)y == (int)z || (int)x + (int)z == (int)y || (int)y + (int)z == (int)x;
    }
}
```