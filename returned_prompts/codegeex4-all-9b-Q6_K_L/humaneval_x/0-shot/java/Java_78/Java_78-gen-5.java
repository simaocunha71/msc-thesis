```java
import java.util.*;
import java.lang.*;

class Solution {
    public int hexKey(String num) {
        char[] hexDigits = num.toCharArray();
        int count = 0;
        for (char hexDigit : hexDigits) {
            if (hexDigit == '2' || hexDigit == '3' || hexDigit == '5' || hexDigit == '7' || hexDigit == 'B' || hexDigit == 'D') {
                count++;
            }
        }
        return count;
    }
}
```