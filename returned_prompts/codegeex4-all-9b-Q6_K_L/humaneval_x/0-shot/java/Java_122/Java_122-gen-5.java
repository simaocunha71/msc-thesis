```java
import java.util.*;
import java.lang.*;

class Solution {
    public int addElements(List<Integer> arr, int k) {
        int sum = 0;

        for (int i = 0; i < k; i++) {
            int num = arr.get(i);

            if (num < 10) {
                sum += num;
            } else if (num < 100) {
                sum += num;
            }
        }

        return sum;
    }
}
```