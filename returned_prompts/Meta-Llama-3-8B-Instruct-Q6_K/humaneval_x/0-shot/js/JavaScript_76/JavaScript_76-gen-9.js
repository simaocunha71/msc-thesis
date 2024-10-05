Here is the solution:
```
const isSimplePower = (x, n) => {
  if (x < 1) {
    return false;
  }
  let power = 1;
  while (power * n <= x) {
    if (power * n === x) {
      return true;
    }
    power *= n;
  }
  return false;
};
```
Explanation:

* We start by checking if `x` is less than 1, in which case it's not a simple power of `n`, so we return `false`.
* We then initialize a variable `power` to 1 and start a loop that increments `power` by `n` each iteration.
* In each iteration, we check if `power * n` is equal to `x`. If it is, we return `true`, because `x` is a simple power of `n`.
* If the loop finishes without finding a match, we return `false`, because `x` is not a simple power of `n`.
* The loop terminates when `power * n` exceeds `x`, which ensures that we've checked all possible powers of `n` up to `x`. If `x` is a simple power of `n`, we'll find it in this range. If not, we'll return `false`.