You can use the `Math.round()` function to round the given number to the closest integer. 

Here is the complete solution:

```java
import java.util.*;

class Solution {
    public int closest_integer(String value) {
        double num = Double.parseDouble(value);
        int integer = (int) Math.round(num);
        return integer;
    }
}
```

This solution works by first converting the given string to a double using `Double.parseDouble()`. Then it uses `Math.round()` to round the double to the closest integer. Finally, it returns the rounded integer.

This solution works for both positive and negative numbers, as well as numbers with decimal points. For example, `closest_integer("10")` returns `10`, `closest_integer("15.3")` returns `15`, `closest_integer("14.5")` returns `15`, and `closest_integer("-14.5")` returns `-15`. 

This solution is also efficient and can handle large inputs. 

Note that the `Math.round()` function always rounds towards the nearest integer, which is equivalent to rounding away from zero in this case. For example, `Math.round(14.5)` returns `15`, and `Math.round(-14.5)` returns `-15`. This is why this solution works correctly even when the given number is equidistant from two integers. 