The task is to create a function `isSimplePower` that takes two parameters, `x` and `n`, and returns `true` if `x` is a simple power of `n` and `false` otherwise.

A number `x` is a simple power of `n` if `n` raised to the power of an integer is equal to `x`. For example, `1` is a simple power of `4` because `4^0 = 1`, and `2` is a simple power of `2` because `2^1 = 2`.

Here's a possible implementation of the `isSimplePower` function in JavaScript:
```
const isSimplePower = (x, n) => {
  for (let i = 0; Math.pow(n, i) <= x; i++) {
    if (Math.pow(n, i) === x) {
      return true;
    }
  }
  return false;
};
```
This function uses a `for` loop to iterate over the powers of `n` from `0` to `x`. If `n` raised to the power of `i` is equal to `x`, the function returns `true`. If no such `i` is found, the function returns `false`.

For example, `isSimplePower(1, 4)` returns `true` because `4^0 = 1`, and `isSimplePower(2, 2)` returns `true` because `2^1 = 2`. On the other hand, `isSimplePower(3, 2)` returns `false` because there is no `i` such that `2^i = 3`, and `isSimplePower(5, 3)` returns `false` because there is no `i` such that `3^i = 5`.