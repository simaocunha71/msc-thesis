  let count = 0;
  for (let num of arr) {
    let sum = 0;
    let isNegative = false;
    if (num < 0) {
      isNegative = true;
      num = -num;
    }
    while (num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if (isNegative) {
      sum = -sum;
    }
    if (sum > 0) {
      count++;
    }
  }
  return count;
}
```

