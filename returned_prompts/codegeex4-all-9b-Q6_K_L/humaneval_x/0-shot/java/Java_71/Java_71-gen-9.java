```java
import java.util.*;
import java.lang.*;

class Solution {
    public double triangleArea(double a, double b, double c) {
        if (a + b > c && a + c > b && b + c > a) {
            double s = (a + b + c) / 2;
            return Math.sqrt(s * (s - a) * (s - b) * (s - c));
        } else {
            return -1;
        }
    }
}
```