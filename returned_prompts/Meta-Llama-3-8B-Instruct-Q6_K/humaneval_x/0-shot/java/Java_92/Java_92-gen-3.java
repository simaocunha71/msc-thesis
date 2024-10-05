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
        return a == b + c || a == c + b || b == a + c || b == c + a || c == a + b || c == b + a;
    }
}
```
Explanation:
The given problem is to create a function that takes three numbers as input and returns true if one of the numbers is equal to the sum of the other two. The function should also check if all the input numbers are integers.

The provided code first checks if all the input numbers are instances of the Integer class. If any of the inputs are not instances of Integer, the function returns false.

If all inputs are instances of Integer, the function casts the inputs to integers and checks if any of the following conditions are true:

* a == b + c
* a == c + b
* b == a + c
* b == c + a
* c == a + b
* c == b + a

If any of these conditions are true, the function returns true. Otherwise, it returns false.

This solution correctly solves the problem and handles the edge cases as required. It also ensures that only integer inputs are processed, as per the problem statement.