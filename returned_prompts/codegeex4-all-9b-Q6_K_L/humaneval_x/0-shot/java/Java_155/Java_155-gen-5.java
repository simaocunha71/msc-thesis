```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> evenOddCount(int num) {
        num = Math.abs(num);
        int even = 0, odd = 0;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                even++;
            } else {
                odd++;
            }
            num /= 10;
        }
        return Arrays.asList(even, odd);
    }
}
```