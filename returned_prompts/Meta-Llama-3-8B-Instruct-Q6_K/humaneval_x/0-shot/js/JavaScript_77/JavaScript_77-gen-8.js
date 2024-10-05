```
const iscube = (a) => {
  let root = Math.cbrt(a);
  return Math.round(root) ** 3 === a;
};
```
Explanation:
The function `iscube` takes an integer `a` as input and returns `true` if `a` is a cube of some integer number, and `false` otherwise.

To solve this problem, we use the `Math.cbrt` function, which returns the cube root of `a`. We then round this value to the nearest integer using `Math.round`, and square it to get the cube of the rounded value. We compare this result with `a` to determine if `a` is a cube.

Note that we use `Math.round` instead of `Math.floor` to handle cases where `a` is a perfect cube, but the cube root is not an exact integer. For example, `Math.cbrt(64)` returns `4.0`, which would be rounded to `4` using `Math.floor`, but we want to consider `64` as a perfect cube.

With this implementation, the function should work correctly for all valid inputs, as required by the problem statement.