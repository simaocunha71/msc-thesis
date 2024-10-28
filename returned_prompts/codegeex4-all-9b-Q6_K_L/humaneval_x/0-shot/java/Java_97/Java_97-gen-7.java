```java
public int multiply(int a, int b) {
    return Integer.parseInt(String.valueOf(a).substring(String.valueOf(a).length() - 1)) * Integer.parseInt(String.valueOf(b).substring(String.valueOf(b).length() - 1));
}
```