```
return Math.cbrt(a) % 1 === 0;
```
Explanation:
The `Math.cbrt()` function returns the cube root of a number. If the input number `a` is a perfect cube, then the cube root of `a` will be an integer, which means the remainder when divided by 1 will be 0. Therefore, we can check if the remainder is 0 to determine if `a` is a perfect cube.

For example, `Math.cbrt(27)` returns `3`, which is an integer, so the remainder when divided by 1 is 0. On the other hand, `Math.cbrt(28)` returns `2.512195941444381`, which is not an integer, so the remainder is not 0. This is why we can use `Math.cbrt(a) % 1 === 0` to check if `a` is a perfect cube.