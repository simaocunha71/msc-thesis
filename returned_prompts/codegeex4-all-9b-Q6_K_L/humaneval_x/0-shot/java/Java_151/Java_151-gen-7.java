Here is the Java code that solves the problem:

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
This code defines a method `doubleTheDifference` that takes a list of objects as an argument. It iterates over each object in the list and checks if it is an instance of `Integer`. If it is, it casts the object to an integer and checks if it is positive and odd. If both conditions are true, it adds the square of the number to the `sum` variable. Finally, it returns the `sum` variable.