```java
import java.util.*;
import java.lang.*;

class Solution {
    public String changeBase(int x, int base) {
        if (base < 2 || base > 9) {
            throw new IllegalArgumentException("Base must be between 2 and 9");
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