```java
import java.util.*;
import java.lang.*;

class Solution {
    public String changeBase(int x, int base) {
        if (x < base) {
            return Integer.toString(x);
        }
        return changeBase(x / base, base) + Integer.toString(x % base);
    }
}
```