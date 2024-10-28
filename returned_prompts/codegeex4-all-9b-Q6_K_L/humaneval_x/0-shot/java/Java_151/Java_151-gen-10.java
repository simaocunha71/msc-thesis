Here is the Java code to solve this problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doubleTheDifference(List<Object> lst) {
        int sum = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer) {
                int num = (Integer) obj;
                if (num > 0 && num % 2 != 0) {
                    sum += num * num;
                }
            }
        }
        return sum;
    }
}
```

This code first initializes a sum variable to 0. It then iterates over each object in the input list. If the object is an instance of Integer, it checks if the number is positive and odd. If so, it adds the square of the number to the sum. Finally, it returns the sum.