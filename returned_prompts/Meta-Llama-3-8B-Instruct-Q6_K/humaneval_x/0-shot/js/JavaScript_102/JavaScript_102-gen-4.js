Here is the JavaScript solution for the problem:

```javascript
const chooseNum = (x, y) => {
  if (x > y) {
    [x, y] = [y, x];
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
The function first checks if x is greater than y. If it is, it swaps them. This ensures that we start from the smaller number and iterate up to the larger number.

Then, it iterates over the numbers from x to y (inclusive) and checks if each number is even (i.e., if `i % 2 === 0`). If it finds an even number, it returns that number.

If it doesn't find any even numbers in the range, it returns -1. This means that there were no even numbers in the range [x, y].