```java
import java.util.*;
import java.lang.*;

class Solution {
    public String changeBase(int x, int base) {
        if (x == 0) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        while (x > 0) {
            sb.append(x % base);
            x /= base;
        }
        return sb.reverse().toString();
    }
}
```