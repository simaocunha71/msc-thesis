```java
import java.util.*;
import java.lang.*;

class Solution {
    public int howManyTimes(String string, String substring) {
        int count = 0;
        int subLength = substring.length();
        int stringLength = string.length();

        for (int i = 0; i <= stringLength - subLength; i++) {
            if (string.substring(i, i + subLength).equals(substring)) {
                count++;
            }
        }

        return count;
    }
}
```