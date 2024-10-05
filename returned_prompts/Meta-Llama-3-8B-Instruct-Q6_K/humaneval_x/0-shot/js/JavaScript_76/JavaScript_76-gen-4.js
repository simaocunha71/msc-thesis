Here is a solution using a while loop to calculate the power of n and check if it is equal to x:
```
const isSimplePower = (x, n) => {
  let power = 1;
  let i = 0;
  while (power <= x) {
    if (power === x) {
      return true;
    }
    power *= n;
    i++;
  }
  return false;
};
```
This function initializes a variable `power` to 1 and a counter `i` to 0. It then enters a while loop that continues until `power` is greater than `x`. Inside the loop, it checks if `power` is equal to `x`, and if so, returns `true`. If not, it multiplies `power` by `n` and increments `i`. If the loop completes without finding a match, it returns `false`.

For example, calling `isSimplePower(8, 2)` will return `true` because 2^3 = 8, and calling `isSimplePower(3, 2)` will return `false` because there is no power of 2 that equals 3.