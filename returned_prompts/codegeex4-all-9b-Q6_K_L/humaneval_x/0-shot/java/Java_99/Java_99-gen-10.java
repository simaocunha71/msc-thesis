```java
import java.util.*;
import java.lang.*;

class Solution {
    public int closest_integer(String value) {
        double num = Double.parseDouble(value);
        return (int) Math.round(num);
    }
}
```
This solution uses the `Double.parseDouble()` method to convert the string value to a double. Then, it uses the `Math.round()` method to round the double to the nearest integer. Finally, it casts the result to an int and returns it.