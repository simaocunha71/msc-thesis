```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> getOddCollatz(int n) {
        if (n <= 0) {
            return new ArrayList<>();
        }
        Set<Integer> set = new HashSet<>();
        while (n != 1) {
            if (n % 2 != 0) {
                set.add(n);
            }
            n = n % 2 == 0 ? n / 2 : 3 * n + 1;
        }
        set.add(1);
        return new ArrayList<>(set);
    }
}
```