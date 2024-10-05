Here is a JavaScript function that implements the described behavior:

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

This function first checks if `x` is greater than `y`. If it is, the function returns `-1` because there are no even numbers in the range `[y, x]`.

If `x` is not greater than `y`, the function then loops through all the numbers in the range `[x, y]` and checks if each number is even. If it finds an even number, it returns that number.

If the function doesn't find any even numbers in the range `[x, y]`, it returns `-1`. This is because the problem states that if there are no even numbers in the range, the function should return `-1`.