```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean anyInt(Object x, Object y, Object z) {
        // Check if all inputs are integers
        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) {
            return false;
        }
        int a = (int) x;
        int b = (int) y;
        int c = (int) z;
        // Check if one of the numbers is equal to the sum of the other two
        return (a == b + c) || (a == c + b) || (b == a + c) || (b == c + a) || (c == a + b) || (c == b + a);
    }
}
```

Explanation:
The provided solution checks if all inputs are integers by using the instanceof operator to check if the objects x, y, and z are instances of the Integer class. If any of the inputs are not integers, the function returns false.

Then, the solution converts the objects to integers using a cast. It then checks if one of the numbers is equal to the sum of the other two by using six separate conditions. If any of these conditions are true, the function returns true. Otherwise, it returns false. This ensures that the function returns true only if one of the numbers is equal to the sum of the other two, and all numbers are integers.