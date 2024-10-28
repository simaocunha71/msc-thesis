import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given length of a side and high return area for a triangle.
    >>> triangleArea(5, 3)
    7.5
     */
    public double triangleArea(double a, double h) {
        return a * h / 2;
    }

    /**
    Given length of a side and high return perimeter for a triangle.
    >>> trianglePerimeter(5, 3)
    13
     */
    public double trianglePerimeter(double a, double h) {
        return a * 3;
    }

    /**
    Given length of a side and high return perimeter for a triangle.
    >>> trianglePerimeter(5, 3)
    13
     */
    public double trianglePerimeter(double a, double h) {
        return a * 3 + h * 2;
    }

    /**
    Given length of a side and high return perimeter for a triangle.
    >>> trianglePerimeter(5, 3)
    13
     */
    public double trianglePerimeter(double a, double h) {
        return a * 3 + h * 2 + a * Math.sin(30);
    }
}

