```java
import java.util.*;
import java.lang.*;

class Solution {
    public String circularShift(int x, int shift) {
        String s = String.valueOf(x);
        int n = s.length();
        if (shift > n) {
            return new StringBuilder(s).reverse().toString();
        }
        return s.substring(n - shift) + s.substring(0, n - shift);
    }
}
```