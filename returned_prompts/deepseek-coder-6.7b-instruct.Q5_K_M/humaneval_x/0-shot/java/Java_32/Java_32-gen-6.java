
```

**My Solution:**

```java
import java.util.*;
import java.lang.*;

class Solution {
    public double poly(List<Double> xs, double x) {
        double result = 0;
        for  (int i = 0; i < xs.size(); i++) {
            result += xs.get(i) * Math.pow(x, i);
        }
        return result;
    }

    public double findZero(List<Double> xs) {
        double left = -100;
        double right = 100;
        double mid = (left + right) / 2;

        while (Math.abs(poly(xs, mid)) > 0.00001) {
            if (poly(xs, mid) > 0) {
                right = mid;
            } else {
                left = mid;
            }
            mid = (left + right) / 2;
        }
        return mid;
    }
}
```

**Explanation:**

I solved the problem by applying the Bisection Method. This method is used to find roots of a polynomial equation. It works by taking an initial interval, and dividing it in half until the root is found.

The function `poly(xs, x)` calculates the value of the polynomial at the given point.

The function `findZero(xs)` takes a list of coefficients of a polynomial and returns the root of the polynomial. It uses the Bisection Method to find the root. It starts with an initial interval `[-100, 100]` and calculates the midpoint of this interval. If the value of the polynomial at the midpoint is positive, it sets the new right end of the interval to be the midpoint. If the value of the polynomial at the midpoint is negative, it sets the new left end of the interval to be the midpoint. It repeats this process until the value of the polynomial at the midpoint is close enough to zero (i.e., less than 0.00001).

This process guarantees that the root will be found within the interval `[-100, 100]`.

The B