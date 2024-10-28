```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isMultiplyPrime(int a) {
        int count = 0;
        for (int i = 2; i < a; i++) {
            if (a % i == 0) {
                count++;
                a /= i;
                i--;
            }
        }
        return count == 3;
    }
}
```