  const mean = numbers.reduce((accum, curr) => accum + curr, 0) / numbers.length;
  const differences = numbers.map(number => Math.abs(number - mean));
  const mad = differences.reduce((accum, curr) => accum + curr, 0) / numbers.length;
  
  return mad;
};

console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])); // 1.0
```

</details>


## 3. Write a JavaScript function that calculates the sum of the squares of the absolute differences between each element and its mean.

<details>
  <summary>Solution</summary>

