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
        if (a + b > c || a + c > b || c + b > a) return -1; // invalid triangle
        
	// base
	double min = Math.min(Math.min(a,b),c); 
	double max = Math.max(Math.max(a,b),c);
	if (min <= 0 || max < min) return -1; //invalid triangle
	
	// area
	return Math.abs((max * (max - a) / 2));
    }
}