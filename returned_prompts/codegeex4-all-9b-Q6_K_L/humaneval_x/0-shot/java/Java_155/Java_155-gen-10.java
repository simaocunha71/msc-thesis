```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> evenOddCount(int num) {
        String s = String.valueOf(Math.abs(num));
        int evenCount = 0;
        int oddCount = 0;
        for (char c : s.toCharArray()) {
            int digit = Character.getNumericValue(c);
            if (digit % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }
        return Arrays.asList(evenCount, oddCount);
    }
}
```