```java
import java.util.*;
import java.lang.*;

class Solution {
    public int howManyTimes(String string, String substring) {
        if (substring.isEmpty()) {
            return 0;
        }
        int count = 0;
        int index = 0;
        while (true) {
            index = string.indexOf(substring, index);
            if (index == -1) {
                break;
            }
            count++;
            index++;
        }
        return count;
    }
}
```
