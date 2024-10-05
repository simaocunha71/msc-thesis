        // write your code here

    }
}


A: Here is the solution in Java:

```java
public double triangleArea(double a, double b, double c) {

    // check if the three sides form a valid triangle
    if (a + b > c && a + c > b && b + c > a) {
        // calculate semi-perimeter
        double s = (a + b + c) / 2;
        // calculate area using Heron's formula
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        // round to 2 decimal places
        return Math.round(area * 100.0) / 100.0;
    } else {
        // return -1 if the triangle is invalid
        return -1;
    }
}
```

Here is the explanation of the solution:

1. First, the function checks if the three sides form a valid triangle. A valid triangle should satisfy the triangle inequality principle, i.e., the sum of the lengths of any two sides must be greater than the length of the third side.

2. If the triangle is valid, the function calculates the semi-perimeter of the triangle, which is half the sum of the lengths of the three sides.

3. The area of the triangle is calculated using Heron's formula. Heron's formula gives the area of a triangle given the lengths of the three sides a, b, and c.

4. The area is then rounded to 2 decimal places using the Math.round() function.

5. If the triangle is not valid, the function returns -1.

This solution assumes that the lengths of the sides are given in the same units (e.g., centimeters), which is the most common use case for this problem. If the lengths are given in different units, the function will need to be adjusted accordingly.

Note: This solution uses Math.sqrt() to calculate the square root and Math.round() to round the area to 2 decimal places. These are built-in Java functions that perform these calculations.

The time complexity of this solution is O(1), i.e., it takes constant time regardless of the input size. The space