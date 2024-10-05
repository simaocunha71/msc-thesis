```javascript
const isSimplePower = (x, n) => {
  if (x < 1) return false;
  const root = Math.pow(n, Math.floor(Math.log(x) / Math.log(n)));
  return root === Math.pow(n, root);
};
```



Explanation:
The function `isSimplePower` takes two arguments, `x` and `n`, and returns a boolean value indicating whether `x` is a simple power of `n` or not.

The function first checks if `x` is less than 1, in which case it returns `false` because `x` cannot be a simple power of `n` for any `n`.

Next, it calculates the root of `x` using the formula `root = n^floor(log(x) / log(n))`. This is done using the `Math.pow` function to calculate the power of `n` and the `Math.floor` function to calculate the floor of the result of the logarithm.

Finally, it checks if the root is equal to the power of `n` to the power of the root. If it is, then `x` is a simple power of `n`, and the function returns `true`. Otherwise, it returns `false`.

For example, if `x` is 8 and `n` is 2, the function will calculate the root as 2^2, which is equal to 4, and then check if 4 is equal to 2^4, which it is. Therefore, the function will return `true`. If `x` is 3 and `n` is 2, the function will calculate the root as 2^1.5, which is not an integer, so the function will return `false`.