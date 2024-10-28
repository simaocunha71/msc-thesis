```java
import java.util.*;
import java.lang.*;

class Solution {
    public double poly(List<Double> xs, double x) {
        double result = 0;
        for (int i = 0; i < xs.size(); i++) {
            result += xs.get(i) * Math.pow(x, i);
        }
        return result;
    }

    public double findZero(List<Double> xs) {
        double x = 0.0;
        double h = 0.01;
        double fx = poly(xs, x);
        while (fx != 0) {
            x += h;
            fx = poly(xs, x);
        }
        return x;
    }
}
```