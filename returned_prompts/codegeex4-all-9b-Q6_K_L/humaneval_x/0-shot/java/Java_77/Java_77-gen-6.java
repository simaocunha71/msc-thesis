You can use the cube root function to solve this problem. Here is the solution:

```java
public boolean iscube(int a) {
    double cbrt = Math.cbrt(a);
    return (cbrt == Math.floor(cbrt));
}
```

The `Math.cbrt` function returns the cube root of a number. We then compare it to `Math.floor(cbrt)`, which returns the largest integer less than or equal to the cube root. If the cube root is an integer, these two numbers should be equal. So, if `Math.cbrt(a) == Math.floor(cbrt)`, then `a` is a cube of some integer number.