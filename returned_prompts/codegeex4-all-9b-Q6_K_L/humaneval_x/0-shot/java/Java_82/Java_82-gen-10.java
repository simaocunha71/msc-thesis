```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean primeLength(String string) {
        int n = string.length();
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```