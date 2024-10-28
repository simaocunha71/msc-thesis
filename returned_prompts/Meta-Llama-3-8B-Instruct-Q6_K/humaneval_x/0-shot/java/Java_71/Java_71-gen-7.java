```java
import java.util.*;

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
        if (a + b <= c || a + c <= b || b + c <= a) {
            return -1.0;
        }
        double s = (a + b + c) / 2.0;
        return Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)) * 100.0) / 100.0;
    }
}
```
Explanation: 
This code checks if the three sides of the triangle form a valid triangle by using the triangle inequality theorem. 
If the sum of any two sides is less than or equal to the third side, then the three sides do not form a valid triangle, so the function returns -1.0.
If the three sides form a valid triangle, then the function calculates the semi-perimeter 's' of the triangle using the formula s = (a + b + c) / 2.0.
Then it calculates the area of the triangle using Heron's formula, which is sqrt(s * (s - a) * (s - b) * (s - c)).
The area is then rounded to 2 decimal points using the Math.round() function. 
The result is returned as a double value. 
This solution has a time complexity of O(1) and a space complexity of O(1), as it only uses a constant amount of space to store the variables and does not use any data structures that scale with the input size. 