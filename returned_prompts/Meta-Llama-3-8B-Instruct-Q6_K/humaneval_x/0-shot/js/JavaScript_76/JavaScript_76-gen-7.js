```javascript
const isSimplePower = (x, n) => {
  let base = 1;
  while (base ** n <= x) {
    if (base ** n === x) {
      return true;
    }
    base++;
  }
  return false;
};
```



Here is the explanation:

The function `isSimplePower` checks if a number `x` is a simple power of `n`. It does this by iterating through all possible base values starting from 1 until it finds a base value that raises to the power of `n` equals to `x`. If it finds such a base value, it returns `true`. If it doesn't find any such base value after iterating through all possible base values, it returns `false`.

Here's how it works:

1. Initialize a variable `base` to 1.
2. Enter a while loop that continues until `base` raised to the power of `n` is less than or equal to `x`.
3. Inside the loop, check if `base` raised to the power of `n` equals to `x`. If it does, return `true`.
4. If the condition in step 3 is not met, increment `base` by 1 and continue to the next iteration.
5. If the loop completes without finding a match, return `false`.

This function uses a simple and efficient approach to solve the problem, with a time complexity of O(log x) because it iterates through the base values in a logarithmic manner.