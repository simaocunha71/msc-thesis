Here is the JavaScript solution for the problem:

```javascript
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

Explanation:
The function `chooseNum` takes two parameters, `x` and `y`, which are positive numbers. If `x` is greater than `y`, the function returns `-1` because there is no even number in the range `[x, y]`.

Then, the function iterates from `x` to `y` using a `for` loop. For each number `i` in the range, it checks if `i` is even by using the modulus operator `%`. If `i` is even (i.e., `i % 2 === 0`), the function returns `i` as the biggest even number in the range.

If the function does not find any even number in the range, it returns `-1` at the end of the function. This is because the problem statement requires the function to return `-1` if there is no even number in the range.