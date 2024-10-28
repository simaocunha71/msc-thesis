```java
import java.util.*;
import java.lang.*;

class Solution {
    public int hexKey(String num) {
        int count = 0;
        for (char c : num.toCharArray()) {
            if (c == '2' || c == '3' || c == '5' || c == '7' || c == 'B' || c == 'D') {
                count++;
            }
        }
        return count;
    }
}
```