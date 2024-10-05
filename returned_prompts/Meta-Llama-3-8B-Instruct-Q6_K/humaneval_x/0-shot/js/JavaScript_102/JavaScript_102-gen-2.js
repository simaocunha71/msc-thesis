Here is the solution in JavaScript:
```
const chooseNum = (x, y) => {
  if (x > y) {
    return -1;
  }
  for (let i = x; i <= y; i++) {
    if (i % 2 === 0) {
      return i;
    }
  }
  return -1;
};
```
Here's an explanation of the code:

1. We first check if `x` is greater than `y`. If it is, we return -1, because there's no even number in the range `[x, y]`.
2. We then loop through all numbers from `x` to `y` (inclusive) using a `for` loop.
3. For each number, we check if it's even by using the modulo operator (`%`). If the remainder is 0, it means the number is even.
4. If we find an even number, we return it immediately.
5. If we reach the end of the loop without finding an even number, we return -1, indicating that there's no even number in the range.

