```java
import java.util.*;
import java.lang.*;

class Solution {
    public int maxElement(List<Integer> l) {
        int max = Integer.MIN_VALUE;
        for (int num : l) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }
}
```