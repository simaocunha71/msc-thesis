```
return Math.cbrt(a) % 1 === 0;
```

Explanation:
The `Math.cbrt()` function calculates the cube root of a number. If the input `a` is a perfect cube, then the cube root of `a` will be an integer. The `% 1 === 0` checks if the remainder of the division of the cube root by 1 is 0, which is true if the number is an integer.

For example, `Math.cbrt(64)` returns `4`, which is an integer, so `iscube(64)` returns `true`. On the other hand, `Math.cbrt(180)` returns `4.74257...`, which is not an integer, so `iscube(180)` returns `false`.