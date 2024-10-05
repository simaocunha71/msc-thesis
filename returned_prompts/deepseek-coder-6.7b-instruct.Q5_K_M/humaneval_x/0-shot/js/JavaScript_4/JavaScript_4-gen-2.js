  const mean = numbers.reduce((acc, val) => acc + val, 0) / numbers.length;
  const differences = numbers.map(number => Math.abs(number - mean));
  return differences.reduce((acc, val) => acc + val, 0) / numbers.length;
}

console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])); // 1.0
```

## Standard Deviation

```javascript
