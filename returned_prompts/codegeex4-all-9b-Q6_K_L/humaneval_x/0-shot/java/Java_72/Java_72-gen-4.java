```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean willItFly(List<Integer> q, int w) {
        return isPalindrome(q) && sum(q) <= w;
    }

    private boolean isPalindrome(List<Integer> list) {
        int size = list.size();
        for (int i = 0; i < size / 2; i++) {
            if (!Objects.equals(list.get(i), list.get(size - 1 - i))) {
                return false;
            }
        }
        return true;
    }

    private int sum(List<Integer> list) {
        int sum = 0;
        for (int num : list) {
            sum += num;
        }
        return sum;
    }
}
```