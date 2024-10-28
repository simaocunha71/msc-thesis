```java
public double triangleArea(double a, double b, double c) {
    double area = -1;
    if (a + b > c && a + c > b && b + c > a) {
        double s = (a + b + c) / 2;
        area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
    return Math.round(area * 100.0) / 100.0;
}
```