```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> getOddCollatz(int n) {
        List<Integer> list = new ArrayList<>();
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                list.add(n);
                n = 3 * n + 1;
            }
        }
        list.add(1);
        Collections.sort(list);
        return list;
    }
}
```