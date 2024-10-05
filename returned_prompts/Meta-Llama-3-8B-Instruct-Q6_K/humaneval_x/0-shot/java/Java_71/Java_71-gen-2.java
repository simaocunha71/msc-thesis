```java
import java.util.*;

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

Explanation:
The problem asks to find the area of a triangle given the lengths of its three sides. The area can be calculated using Heron's formula, which is applicable only when the three sides form a valid triangle.

To check if the three sides form a valid triangle, we can apply the triangle inequality theorem, which states that the sum of any two sides of a triangle is greater than the third side. We can write this condition as:

a + b > c
a + c > b
b + c > a

If these conditions are met, then the three sides form a valid triangle, and we can calculate the area using Heron's formula. Otherwise, we return -1.

The code implements this logic. It first checks if the three sides form a valid triangle using the triangle inequality theorem. If they do, it calculates the semi-perimeter of the triangle (s = (a + b + c) / 2) and uses Heron's formula to calculate the area (Math.sqrt(s * (s - a) * (s - b) * (s - c))). If the three sides do not form a valid triangle, it returns -1. The result is rounded to 2 decimal points using the `Math.round()` function. However, since the problem statement does not specify the precision of the result, we use the `Math.sqrt()` function to get the result in decimal points. If you want to round the result to a specific number of decimal points, you can use the `String.format()` function or a similar method.