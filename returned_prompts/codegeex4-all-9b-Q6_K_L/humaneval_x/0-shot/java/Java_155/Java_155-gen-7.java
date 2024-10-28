```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> evenOddCount(int num) {
        String numStr = String.valueOf(Math.abs(num));
        int evenCount = 0, oddCount = 0;
        for (char c : numStr.toCharArray()) {
            if (Character.isDigit(c)) {
                int digit = Character.getNumericValue(c);
                if (digit % 2 == 0) {
                    evenCount++;
                } else {
                    oddCount++;
                }
            }
        }
        return Arrays.asList(evenCount, oddCount);
    }
}
```