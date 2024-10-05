Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public boolean anyInt(Object x, Object y, Object z) {
        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) {
            return false;
        }
        int a = (int) x;
        int b = (int) y;
        int c = (int) z;
        return (a == b + c) || (b == a + c) || (c == a + b);
    }
}
```
Explanation:

1. We first check if all three objects are instances of Integer using the `instanceof` operator. If any of them are not, we return false.

2. If all are integers, we cast them to int using the `(int)` operator.

3. Then we use three conditionals to check if one of the numbers is equal to the sum of the other two. If any of these conditions are true, we return true.

4. If none of the conditions are true, we return false.

This solution works for all the examples provided in the problem statement. It checks if the inputs are integers and if one of them is equal to the sum of the other two. If the inputs are not integers or the condition is not met, it returns false.