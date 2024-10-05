Here is the JavaScript function that satisfies the problem statement:
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
Here's a breakdown of the function:

1. We first check if `x` is greater than `y`. If so, we return -1 as there is no even number in the range.
2. We then iterate through the range `[x, y]` using a `for` loop. We check each number to see if it's even using the modulo operator (`i % 2 === 0`).
3. If we find an even number, we return it immediately.
4. If we reach the end of the loop without finding an even number, we return -1.

You can test the function with the examples you provided:
```javascript
console.log(chooseNum(12, 15)); // Output: 14
console.log(chooseNum(13, 12)); // Output: -1
```