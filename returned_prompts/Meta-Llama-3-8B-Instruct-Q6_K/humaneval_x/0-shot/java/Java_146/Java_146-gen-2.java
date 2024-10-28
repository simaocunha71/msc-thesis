Here is the Java code that solves the problem:

```java
import java.util.*;

class Solution {
    public int specialFilter(List<Integer> nums) {
        int count = 0;
        for (int num : nums) {
            if (Math.abs(num) > 10) {
                int firstDigit = num / 10;
                int lastDigit = num % 10;
                if (firstDigit % 2 != 0 && lastDigit % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

This code iterates over each number in the input list. If the absolute value of the number is greater than 10, it checks if both the first and last digits are odd (i.e., their remainder when divided by 2 is not 0). If both conditions are met, it increments the count. Finally, it returns the count.