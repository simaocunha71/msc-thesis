```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fizzBuzz(int n) {
        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String numStr = String.valueOf(i);
                for (char c : numStr.toCharArray()) {
                    if (c == '7') {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
```