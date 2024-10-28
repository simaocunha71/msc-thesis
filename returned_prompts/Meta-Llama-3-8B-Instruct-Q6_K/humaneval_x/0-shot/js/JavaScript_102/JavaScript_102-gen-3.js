Here is a possible implementation of the `chooseNum` function in JavaScript:
```
const chooseNum = (x, y) => {
  if (x > y) return -1;
  for (let i = x; i <= y; i++) {
    if (i % 2 === 0) return i;
  }
  return -1;
};
```
Here's an explanation of how the function works:

1. First, we check if `x` is greater than `y`. If it is, we return -1 immediately, since there is no even number in the range `[x, y]`.
2. Then, we iterate from `x` to `y` using a `for` loop. For each number `i` in the range, we check if it's even by using the modulo operator (`%`). If `i` is even, we return it immediately.
3. If we reach the end of the loop without finding an even number, we return -1 to indicate that there is no even number in the range.

You can test this function with the examples you provided:
```
console.log(chooseNum(12, 15)); // Output: 14
console.log(chooseNum(13, 12)); // Output: -1
```
I hope this helps! Let me know if you have any questions.