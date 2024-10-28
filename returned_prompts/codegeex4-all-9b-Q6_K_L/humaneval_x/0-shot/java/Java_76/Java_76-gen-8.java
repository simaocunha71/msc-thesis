```java
public boolean isSimplePower(int x, int n) {
    if (x <= 0 || n <= 0) {
        return false;
    }
    int power = 1;
    while (power < x) {
        power *= n;
        if (power == x) {
            return true;
        }
    }
    return false;
}
```
