```java
import java.util.*;
import java.lang.*;

class Solution {
    public int hexKey(String num) {
        List<Character> primeHexDigits = Arrays.asList('2', '3', '5', '7', 'B', 'D');
        int count = 0;
        for (char c : num.toCharArray()) {
            if (primeHexDigits.contains(c)) {
                count++;
            }
        }
        return count;
    }
}
```