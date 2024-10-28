  const mean = numbers.reduce((acc, val) => acc + val, 0) / numbers.length;

  const differences = numbers.map(number => Math.abs(number - mean));

  const mad = differences.reduce((acc, val) => acc + val, 0) / numbers.length;

  return mad;
};

console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0]));
```


## 5. Binary to Decimal Converter:

