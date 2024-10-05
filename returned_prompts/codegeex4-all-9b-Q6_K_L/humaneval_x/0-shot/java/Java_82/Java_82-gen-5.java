```java
public boolean primeLength(String string) {
    // check if the length of the string is a prime number
    int length = string.length();
    if (length <= 1) return false;
    for (int i = 2; i <= Math.sqrt(length); i++) {
        if (length % i == 0) return false;
    }
    return true;
}
```