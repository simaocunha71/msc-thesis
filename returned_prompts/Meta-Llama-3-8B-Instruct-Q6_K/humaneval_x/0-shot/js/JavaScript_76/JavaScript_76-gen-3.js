```javascript
const isSimplePower = (x, n) => {
  if (n <= 0) return false;
  let base = 1;
  while (base * base <= x) {
    if (base * base === x) return true;
    base++;
  }
  return false;
};
```


The function `isSimplePower` takes two arguments, `x` and `n`. It checks if `x` is a simple power of `n`.

First, it checks if `n` is less than or equal to 0. If it is, the function immediately returns `false`, as a simple power of a non-positive integer does not exist.

Then, it initializes a variable `base` to 1. This variable will be used to check if `x` is a simple power of `n`.

The function then enters a while loop, which continues as long as `base * base` is less than or equal to `x`. Inside the loop, it checks if `base * base` is equal to `x`. If it is, the function returns `true`, indicating that `x` is a simple power of `n`.

If the loop completes without finding a match, the function returns `false`, indicating that `x` is not a simple power of `n`.

This function works by iteratively checking if `x` is a perfect square (i.e., the square of an integer). If it is, the function returns `true`. If it is not, the function returns `false`. This approach ensures that the function correctly identifies simple powers of `n`.