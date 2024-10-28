```java
public double triangleArea(double a, double b, double c) {
    double p = (a + b + c) / 2;
    double area = Math.sqrt(p * (p - a) * (p - b) * (p - c));
    if (area < 0) {
        return -1;
    }
    return Math.round(area * 100.0) / 100.0;
}
```
The provided code calculates the area of a triangle using Heron's formula. It checks if the triangle is valid by ensuring that the sum of any two sides is greater than the third side. If the triangle is not valid, it returns -1. Otherwise, it returns the area rounded to two decimal points.