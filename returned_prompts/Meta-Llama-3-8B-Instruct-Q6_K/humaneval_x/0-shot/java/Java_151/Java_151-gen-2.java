```java
import java.util.*;

class Solution {
    public int doubleTheDifference(List<Object> lst) {
        int sum = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer && ((Integer) obj) > 0) {
                sum += Math.pow((Integer) obj, 2);
            }
        }
        return sum;
    }
}
```
Explanation:
The problem asks to calculate the sum of squares of the odd numbers in the list. We iterate over the list and check each element if it is an integer and positive. If it is, we add its square to the sum. We use the `Math.pow` method to calculate the square of the number. Finally, we return the sum. If the list is empty, the method returns 0.