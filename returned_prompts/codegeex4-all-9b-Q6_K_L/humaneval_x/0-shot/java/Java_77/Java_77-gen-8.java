```java
public boolean iscube(int a) {
    if (a == 0) {
        return true;
    }
    double root = Math.cbrt(a);
    return Math.abs(root - Math.floor(root)) < 1e-9;
}
```