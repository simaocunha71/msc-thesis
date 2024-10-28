  const mean = numbers.reduce((acc, num) => acc + num, 0) / numbers.length;
  const differences = numbers.map(num => Math.abs(num - mean));
  const mad = differences.reduce((acc, num) => acc + num, 0) / numbers.length;
  return mad;
};

console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])); // 1.0
```

## Problem 12

```javascript
