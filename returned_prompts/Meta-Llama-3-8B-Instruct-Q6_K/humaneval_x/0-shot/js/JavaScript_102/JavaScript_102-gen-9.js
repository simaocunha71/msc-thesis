Here is a possible implementation of the function `chooseNum`:
```
const chooseNum = (x, y) => {
  if (x > y) return -1; // if x is greater than y, there's no even number in the range
  for (let i = x; i <= y; i++) {
    if (i % 2 === 0) return i; // if we find an even number, return it
  }
  return -1; // if we didn't find an even number, return -1
};
```
Here's an explanation of the code:

1. We first check if `x` is greater than `y`. If it is, we return -1 immediately, because there's no even number in the range.
2. We then use a `for` loop to iterate from `x` to `y` (inclusive).
3. Inside the loop, we check if the current number `i` is even by using the modulo operator (`%`). If `i` is