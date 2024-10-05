```java
public boolean rightAngleTriangle(int a, int b, int c) {
    int max = Math.max(a, Math.max(b, c));
    return Math.pow(max, 2) == Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(c, 2) - Math.pow(max, 2);
}
```