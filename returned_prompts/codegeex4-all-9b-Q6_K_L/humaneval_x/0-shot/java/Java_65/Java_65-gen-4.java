```java
import java.util.*;
import java.lang.*;

class Solution {
    public String circularShift(int x, int shift) {
        String result = Integer.toString(x);
        if (shift > result.length()) {
            return new StringBuilder(result).reverse().toString();
        } else {
            return result.substring(result.length() - shift) + result.substring(0, result.length() - shift);
        }
    }
}
```