Here is a Java solution for the problem:

```java
public String changeBase(int x, int base) {
    StringBuilder sb = new StringBuilder();
    while (x > 0) {
        sb.insert(0, x % base);
        x = x / base;
    }
    return sb.toString();
}
```

This solution uses a StringBuilder to build the result string. It repeatedly divides the input number by the target base, prepending the remainder to the result string. This process continues until the input number becomes 0. The result string is then returned.

For example, if we call `changeBase(8, 3)`, the function will return `"22"`, because 8 in base 3 is 22. If we call `changeBase(8, 2)`, the function will return `"1000"`, because 8 in base 2 is 1000. If we call `changeBase(7, 2)`, the function will return `"111"`, because 7 in base 2 is 111.