```java
public boolean rightAngleTriangle(int a, int b, int c) {
    return (a*a + b*b == c*c) || (a*a + c*c == b*b) || (b*b + c*c == a*a);
}
```