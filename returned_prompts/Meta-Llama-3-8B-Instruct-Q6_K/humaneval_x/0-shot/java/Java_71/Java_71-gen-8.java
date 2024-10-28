```java
import java.util.*;

public class Solution {
    public double triangleArea(double a, double b, double c) {
        // Check if the three sides form a valid triangle
        if (a + b <= c || a + c <= b || b + c <= a) {
            return -1; // Return -1 if the sides do not form a valid triangle
        }

        // Calculate the semi-perimeter of the triangle
        double s = (a + b + c) / 2;

        // Calculate the area of the triangle using Heron's formula
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));

        // Return the area rounded to 2 decimal points
        return Math.round(area * 100.0) / 100.0;
    }
}
```

Explanation:

This problem requires us to find the area of a triangle given the lengths of its sides. However, before calculating the area, we need to check if the three sides form a valid triangle. This is done by checking if the sum of any two sides is greater than the third side.

If the sides do not form a valid triangle, we return -1. Otherwise, we calculate the semi-perimeter of the triangle using the formula `s = (a + b + c) / 2`.

We then use Heron's formula to calculate the area of the triangle: `area = sqrt(s * (s - a) * (s - b) * (s - c))`.

Finally, we return the area rounded to 2 decimal points using the `Math.round` method. We multiply the area by 100.0 to shift the decimal point to the left, and then divide by 100.0 to round it to 2 decimal points. This ensures that the returned area is accurate to 2 decimal points.