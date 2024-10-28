```java
import java.util.*;

class Solution {
    public boolean triplesSumToZero(List<Integer> l) {
        Collections.sort(l);
        for (int i = 0; i < l.size() - 2; i++) {
            int j = i + 1;
            int k = l.size() - 1;
            while (j < k) {
                int sum = l.get(i) + l.get(j) + l.get(k);
                if (sum == 0) {
                    return true;
                } else if (sum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }
        return false;
    }
}
```