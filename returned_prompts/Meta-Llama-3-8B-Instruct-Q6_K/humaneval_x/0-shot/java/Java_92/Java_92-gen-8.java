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
        return (a == b + c) || (a == c + b) || (b == a + c) || (b == c + a) || (c == a + b) || (c == b + a);
    }
}
```
The given problem requires a function that takes three numbers as input and returns `true` if one of the numbers is equal to the sum of the other two. The function should also return `true` if all numbers are integers. If the numbers are not integers, the function should return `false`.

In the provided Java solution, we first check if all the input objects are instances of `Integer`. If not, we immediately return `false`. Then, we cast the objects to `int` and check if any of the following conditions are true:

* `a` is equal to the sum of `b` and `c`
* `a` is equal to the sum of `c` and `b`
* `b` is equal to the sum of `a` and `c`
* `b` is equal to the sum of `c` and `a`
* `c` is equal to the sum of `a` and `b`
* `c` is equal to the sum of `b` and `a`

If any of these conditions are true, we return `true`. Otherwise, we return `false`. This solution ensures that the function returns the correct result for all possible input combinations.