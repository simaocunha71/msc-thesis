```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean rightAngleTriangle(int a, int b, int c) {
        if(a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a) {
            return true;
        } else {
            return false;
        }
    }
}
```