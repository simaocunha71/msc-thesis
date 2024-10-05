```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle.
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater
    than the third side.
    Example:
    triangleArea(3, 4, 5) == 6.00
    triangleArea(1, 2, 10) == -1
     */
    public double triangleArea(double a, double b, double c) {
        // Check if the three sides form a valid triangle
        if (a + b <= c || a + c <= b || b + c <= a) {
            return -1; // Return -1 if the three sides do not form a valid triangle
        }
        // Calculate the semi-perimeter
        double s = (a + b + c) / 2;
        // Calculate the area using Heron's formula
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        // Return the area rounded to 2 decimal points
        return Math.round(area * 100.0) / 100.0;
    }
}
```
Explanation:
The code defines a method `triangleArea` that takes three arguments `a`, `b`, and `c` representing the lengths of the three sides of a triangle. The method first checks if the three sides form a valid triangle by verifying if the sum of any two sides is greater than the third side. If the three sides do not form a valid triangle, the method returns -1.

If the three sides form a valid triangle, the method calculates the semi-perimeter `s` and uses Heron's formula to calculate the area of the triangle. The area is then rounded to 2 decimal points using the `Math.round` method. The result is returned as a `double` value.

The example code snippet demonstrates the usage of the `triangleArea` method with two different sets of input values: `(3, 4, 5)` and `(1, 2, 10)`. The output for the first set of input values is `6.00`, indicating that the three sides form a valid triangle with an area of 6. The output for the second set of input values is `-1`,