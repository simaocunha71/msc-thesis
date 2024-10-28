```java
import java.util.*;
import java.lang.*;

class Solution {
    public String changeBase(int x, int base) {
        String digits = "0123456789";
        StringBuilder sb = new StringBuilder();
        while (x > 0) {
            sb.append(digits.charAt(x % base));
            x /= base;
        }
        return sb.reverse().toString();
    }
}
```