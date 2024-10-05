```java
public double triangleArea(double a, double b, double c) {
    // Check if the given sides can form a triangle
    if (a + b <= c || a + c <= b || b + c <= a) {
        return -1.0;
    }

    // Calculate the semi-perimeter of the triangle
    double s = (a + b + c) / 2;

    // Calculate the area of the triangle using Heron's formula
    double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));

    // Round the area to 2 decimal points
    return Math.round(area * 100.0) / 100.0;
}
```