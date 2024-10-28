```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> getOddCollatz(int n) {
        Set<Integer> oddCollatz = new HashSet<>();
        while (n != 1) {
            if (n % 2 != 0) {
                oddCollatz.add(n);
            }
            n = n % 2 == 0 ? n / 2 : 3 * n + 1;
        }
        oddCollatz.add(1);
        List<Integer> result = new ArrayList<>(oddCollatz);
        Collections.sort(result);
        return result;
    }
}
```