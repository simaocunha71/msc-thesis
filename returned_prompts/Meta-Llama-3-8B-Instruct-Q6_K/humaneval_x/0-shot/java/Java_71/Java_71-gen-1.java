The problem is asking to find the area of a triangle given the lengths of its three sides. The area of a triangle can be calculated using the formula `(b * c) / 2`, where `b` and `c` are the base and height of the triangle. However, this formula assumes that the height is given, which is not the case in this problem.

To solve this problem, we need to find the height of the triangle first. We can do this by using the law of cosines, which states that `c^2 = a^2 + b^2 - 2ab * cos(C)`, where `C` is the angle opposite side `c`. Solving for `cos(C)`, we get `cos(C) = (a^2 + b^2 - c^2) / (2ab)`.

Now we can use the formula for the area of a triangle to calculate the area. The formula is `(b * c) / 2 * sin(C)`, where `sin(C) = sqrt(1 - cos^2(C))`.

Here is the Java code that implements this solution:
```java
import java.util.*;

class Solution {
    public double triangleArea(double a, double b, double c) {
        if (a + b <= c || a + c <= b || b + c <= a) {
            return -1; // The three sides do not form a valid triangle
        }
        double cosC = (a * a + b * b - c * c) / (2 * a * b);
        double sinC = Math.sqrt(1 - cosC * cosC);
        return (b * c) / 2 * sinC;
    }
}
```
This code first checks if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If they do not form a valid triangle, the method returns -1. If they do form a valid triangle, the method calculates the area using the formula `(b * c) / 2 * sin(C)`. The `sin(C)` is calculated using the law of cosines and the `Math.sqrt` function. The area is then returned rounded to 2 decimal points.