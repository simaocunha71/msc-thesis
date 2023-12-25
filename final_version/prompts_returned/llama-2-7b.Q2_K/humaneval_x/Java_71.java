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
        if (a + b > c || a + c > b || a + c > b) return -1.0;
        else if ((b * b + b * c + c * c + 2 * a * b + 2 * a * c + 4 * a * b) >= Math.pow(c, 2)) {
            double ans = (a + b + c) / 2;
            return Math.round(ans * 0.01);
        } else {
            return -1;
        }
    }
}