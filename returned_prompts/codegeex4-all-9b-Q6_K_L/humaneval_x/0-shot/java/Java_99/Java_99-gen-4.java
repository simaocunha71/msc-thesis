```java
import java.util.*;
import java.lang.*;

class Solution {
    public int closest_integer(String value) {
        double num = Double.parseDouble(value);
        int closest = (int) Math.round(num);
        if (Math.abs(num - closest) == 0.5) {
            return (int) Math.signum(num) * (Math.abs(closest) + 1);
        }
        return closest;
    }
}
```