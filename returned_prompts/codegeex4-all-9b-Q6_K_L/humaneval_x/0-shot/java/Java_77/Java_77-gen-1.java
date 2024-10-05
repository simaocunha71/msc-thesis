You can use the Math.cbrt() function to check if the cube root of a number is an integer.
Here is the solution:

```java
public boolean iscube(int a) {
    double cbrt = Math.cbrt(a);
    return cbrt == Math.floor(cbrt);
}
```