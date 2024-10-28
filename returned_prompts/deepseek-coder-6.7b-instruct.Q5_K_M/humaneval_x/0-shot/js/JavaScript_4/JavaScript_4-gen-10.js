  const mean = numbers.reduce((accum, val) => accum + val, 0) / numbers.length;
  const differences = numbers.map(num => Math.abs(num - mean));
  const mad = differences.reduce((accum, val) => accum + val, 0) / numbers.length;
  return mad;
};

console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])); // 1.0
```

## Mean Squared Error

