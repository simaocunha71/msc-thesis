Here is a Java solution:

```java
public double triangleArea(double a, double b, double c) {
    if (a + b > c && a + c > b && b + c > a) {
        double s = (a + b + c) / 2;
        return Math.round((Math.sqrt(s * (s - a) * (s - b) * (s - c))) * 100.0) / 100.0;
    } else {
        return -1;
    }
}
```

This solution first checks if the three sides can form a valid triangle by verifying the triangle inequality. If they do, it calculates the area using Heron's formula and rounds it to 2 decimal points. If the sides do not form a valid triangle, it returns -1. 

The formula used is: `area = sqrt(s * (s - a) * (s - b) * (s - c))`, where `s` is the semi-perimeter of the triangle: `s = (a + b + c) / 2`. This formula works because it calculates the area of the triangle as half the base times the height. In this case, the base is the length of one side, and the height is the distance from the opposite vertex to the midpoint of the base. 

Note that the `Math.round` method is used to round the area to 2 decimal points. The `* 100.0` is used to convert the area to an integer, and then the `/ 100.0` is used to convert it back to a double with 2 decimal points.  This is because `Math.round` rounds to the nearest integer.  If you want to round to a different number of decimal points, you would need to use a different method.  For example, to round to 3 decimal points, you could use `Math.round(area * 1000.0) / 1000.0`.  To round to 5 decimal points, you could use `Math.round(area * 100000.0) / 100000.0`, and so on.  The number you multiply by determines the number of decimal points the area is rounded to.  The `/` at the end converts the result back to a double.  Without the `/`, the result would be an integer.  If you want to round to a certain number of decimal points, you will need to use this method.  If you want