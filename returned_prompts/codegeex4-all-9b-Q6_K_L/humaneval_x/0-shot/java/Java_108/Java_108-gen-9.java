```java
import java.util.*;
import java.lang.*;

class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            int sum = 0;
            boolean isNegative = num < 0;
            if (isNegative) {
                num = -num;
            }
            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }
            if (isNegative) {
                sum = -sum;
            }
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }
}
```