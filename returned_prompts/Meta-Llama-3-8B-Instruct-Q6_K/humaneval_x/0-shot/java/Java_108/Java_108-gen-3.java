Here is the solution in Java:

```java
import java.util.*;

public class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            if (num >= 0) {
                int sum = 0;
                while (num > 0) {
                    sum += num % 10;
                    num /= 10;
                }
                if (sum > 0) {
                    count++;
                }
            } else {
                num = -num;
                int sum = 0;
                while (num > 0) {
                    sum += num % 10;
                    num /= 10;
                }
                if (sum > 0) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

This function iterates over each number in the array. For each number, it calculates the sum of its digits. If the sum is greater than 0, it increments the count. It handles negative numbers by converting them to positive before calculating the sum of digits. Finally, it returns the count.