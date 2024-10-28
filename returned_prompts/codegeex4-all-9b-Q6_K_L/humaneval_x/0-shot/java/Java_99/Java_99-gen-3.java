Here is a Java solution for your problem using the Math.round() function:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int closest_integer(String value) {
        double num = Double.parseDouble(value);
        return (int)Math.round(num);
    }
}
```
This code first converts the input string to a double value using Double.parseDouble(). Then it rounds this value to the nearest integer using Math.round() and finally returns it as an integer.