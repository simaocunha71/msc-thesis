```java
import java.util.*;
import java.lang.*;

class Solution {
    public int hexKey(String num) {
        List<Character> primes = Arrays.asList('2', '3', '5', '7', 'B', 'D');
        int count = 0;
        for (char c : num.toCharArray()) {
            if (primes.contains(c)) {
                count++;
            }
        }
        return count;
    }
}
```
