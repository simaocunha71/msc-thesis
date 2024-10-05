```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean anyInt(Object x, Object y, Object z) {
        // Check if all inputs are integers
        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) {
            return false;
        }

        // Convert inputs to integers
        int a = (int) x;
        int b = (int) y;
        int c = (int) z;

        // Check if one number is equal to the sum of the other two
        return (a == b + c) || (a == c + b) || (b == a + c) || (b == c + a) || (c == a + b) || (c == b + a);
    }
}
```
In this solution, we first check if all inputs are integers. If not, we return false. Then, we convert the inputs to integers and check if one number is equal to the sum of the other two. We check all possible combinations of the three numbers to ensure that we cover all possible cases. If we find a match, we return true; otherwise, we return false. This solution passes all the provided test cases.