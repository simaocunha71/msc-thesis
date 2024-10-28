```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> evenOddCount(int num) {
        int evenCount = 0;
        int oddCount = 0;
        String numStr = String.valueOf(Math.abs(num));
        for (char c : numStr.toCharArray()) {
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