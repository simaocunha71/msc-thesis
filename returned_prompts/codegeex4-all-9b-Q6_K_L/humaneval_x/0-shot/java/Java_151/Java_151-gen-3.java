Here is the Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doubleTheDifference(List<Object> lst) {
        int sum = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer) {
                int num = (int) obj;
                if (num > 0 && num % 2 != 0) {
                    sum += num * num;
                }
            }
        }
        return sum;
    }
}
```

The `doubleTheDifference` method iterates over each object in the list. If the object is an instance of `Integer` and it is a positive odd number, it adds the square of the number to the sum. Finally, it returns the sum. If the input list is empty or does not contain any positive odd numbers, the method will return 0.