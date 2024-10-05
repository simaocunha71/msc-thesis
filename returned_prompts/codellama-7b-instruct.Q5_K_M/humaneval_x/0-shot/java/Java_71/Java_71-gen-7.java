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
        if(a + b < c || b + c < a || a + c < b){
            return -1;
        }
        double s = (a + b + c) / 2.0;
        return Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)) * 100.0) / 100.0;
    }
}




