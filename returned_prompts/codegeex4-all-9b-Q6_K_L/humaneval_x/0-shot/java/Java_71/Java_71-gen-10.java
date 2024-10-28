```java
public double triangleArea(double a, double b, double c) {
    // Check if the sides form a valid triangle
    if (a + b > c && a + c > b && b + c > a) {
        // Calculate the semi-perimeter
        double s = (a + b + c) / 2;
        // Calculate the area using Heron's formula
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        // Round the area to 2 decimal points
        return Math.round(area * 100.0) / 100.0;
    } else {
        // Return -1 if the sides do not form a valid triangle
        return -1;
    }
}
```