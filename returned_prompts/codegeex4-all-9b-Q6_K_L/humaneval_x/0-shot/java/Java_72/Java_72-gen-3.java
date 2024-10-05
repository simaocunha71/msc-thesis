```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean willItFly(List<Integer> q, int w) {
        int sum = 0;
        for (Integer i : q) {
            sum += i;
        }
        if (sum > w) {
            return false;
        }
        int left = 0;
        int right = q.size() - 1;
        while (left < right) {
            if (!q.get(left).equals(q.get(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```