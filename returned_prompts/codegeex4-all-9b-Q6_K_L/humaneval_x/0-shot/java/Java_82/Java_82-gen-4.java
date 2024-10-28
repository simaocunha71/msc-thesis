```java
public boolean primeLength(String string) {
    if (string.length() < 2) {
        return false;
    }
    for (int i = 2; i <= Math.sqrt(string.length()); i++) {
        if (string.length() % i == 0) {
            return false;
        }
    }
    return true;
}
```