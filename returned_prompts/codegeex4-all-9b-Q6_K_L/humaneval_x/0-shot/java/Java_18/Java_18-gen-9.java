```java
import java.util.*;
import java.lang.*;

class Solution {
    public int howManyTimes(String string, String substring) {
        if (string == null || substring == null || substring.length() > string.length()) {
            return 0;
        }
        int count = 0;
        int index = 0;
        while ((index = string.indexOf(substring, index)) != -1) {
            count++;
            index++;
        }
        return count;
    }
}
```