```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isEqualToSumEven(int n) {
        if(n % 2 != 0) {
            return false;
        }
        if(n < 8) {
            return false;
        }
        int sum = 0;
        for(int i = 2; i <= n; i += 2) {
            sum += i;
        }
        return sum == n;
    }
}
```