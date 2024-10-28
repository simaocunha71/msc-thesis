```java
import java.util.*;
import java.lang.*;

class Solution {
    public int closest_integer(String value) {
        double num = Double.parseDouble(value);
        int closest = (int) Math.round(num);
        return closest;
    }
}
```