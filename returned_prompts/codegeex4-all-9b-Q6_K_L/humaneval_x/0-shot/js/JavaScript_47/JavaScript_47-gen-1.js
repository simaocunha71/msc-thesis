You can use the following code to solve the problem:

```javascript
const median = (l) => {
  let sorted = [...l].sort((a, b) => a - b);
  let len = sorted.length;
  if (len % 2 === 0) {
    return (sorted[len / 2 - 1] + sorted[len / 2]) / 2;
  } else {
    return sorted[Math.floor(len / 2)];
  }
};
```

This code first sorts the array `l` in ascending order using the `sort()` function. Then, it checks if the length of the sorted array is even or odd. If it is even, it returns the average of the two middle numbers. If it is odd, it returns the middle number.