```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean iscube(int a) {
        if(a == 0) {
            return true;
        }
        int sqrt = (int)Math.sqrt(Math.abs(a));
        return sqrt*sqrt == Math.abs(a);
    }
}
```