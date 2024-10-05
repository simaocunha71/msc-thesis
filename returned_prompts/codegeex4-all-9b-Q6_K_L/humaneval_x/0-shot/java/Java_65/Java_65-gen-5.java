```java
import java.util.*;
import java.lang.*;

class Solution {
    public String circularShift(int x, int shift) {
        String digits = Integer.toString(x);
        if (shift > digits.length()) {
            return new StringBuilder(digits).reverse().toString();
        }
        return digits.substring(digits.length() - shift) + digits.substring(0, digits.length() - shift);
    }
}
```
