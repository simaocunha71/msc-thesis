```java
import java.util.*;

public class Solution {
    public double triangleArea(double a, double b, double c) {
        // Check if the three sides form a valid triangle
        if (a + b > c && a + c > b && b + c > a) {
            // Calculate the semi-perimeter
            double s = (a + b + c) / 2;
            // Calculate the area using Heron's formula
            double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
            // Return the area rounded to 2 decimal points
            return Math.round(area * 100.0) / 100.0;
        } else {
            // If the three sides do not form a valid triangle, return -1
            return -1;
        }
    }
}
```


Note: This solution assumes that the input values are valid numbers. It does not handle cases where the input values are not numbers. In a real-world scenario, you would need to add error handling to deal with such cases.