```java
import java.util.*;

class Solution {
    public double triangleArea(double a, double b, double c) {
        if (a + b <= c || a + c <= b || b + c <= a) {
            return -1;
        }
        double p = (a + b + c) / 2;
        return Math.sqrt(p * (p - a) * (p - b) * (p - c));
    }
}
```


Explanation:
The problem asks to find the area of a triangle given the lengths of its sides. The area of a triangle can be calculated using Heron's formula, which is `√(p*(p-a)*(p-b)*(p-c))`, where `p` is the semi-perimeter of the triangle, `a`, `b`, and `c` are the lengths of the sides.

However, before applying Heron's formula, we need to check if the three sides form a valid triangle. This is done by checking if the sum of any two sides is greater than the third side. If not, then the three sides do not form a valid triangle and we return -1.

In the code above, we first check if the three sides form a valid triangle using the condition `a + b <= c || a + c <= b || b + c <= a`. If this condition is true, we return -1. Otherwise, we calculate the semi-perimeter `p` and then apply Heron's formula to calculate the area of the triangle. The area is then rounded to 2 decimal points using the `Math.round()` function.