```java
public boolean rightAngleTriangle(int a, int b, int c) {
    if (a > b && a > c) {
        return Math.pow(a, 2) == Math.pow(b, 2) + Math.pow(c, 2);
    } else if (b > a && b > c) {
        return Math.pow(b, 2) == Math.pow(a, 2) + Math.pow(c, 2);
    } else {
        return Math.pow(c, 2) == Math.pow(a, 2) + Math.pow(b, 2);
    }
}
```