```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isNested(String string) {
        int open = 0;
        int close = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') {
                open++;
            } else if (c == ']') {
                close++;
            }
            if (close > open) {
                return false;
            }
        }
        return open == close;
    }
}
```