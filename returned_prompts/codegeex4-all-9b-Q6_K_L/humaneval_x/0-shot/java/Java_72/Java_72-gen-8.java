```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean willItFly(List<Integer> q, int w) {
        int sum = 0;
        for (Integer num : q) {
            sum += num;
        }
        if (sum > w) {
            return false;
        }
        if (q.size() == 1) {
            return true;
        }
        return isPalindrome(q);
    }

    private boolean isPalindrome(List<Integer> q) {
        int size = q.size();
        for (int i = 0; i < size / 2; i++) {
            if (!q.get(i).equals(q.get(size - 1 - i))) {
                return false;
            }
        }
        return true;
    }
}
```