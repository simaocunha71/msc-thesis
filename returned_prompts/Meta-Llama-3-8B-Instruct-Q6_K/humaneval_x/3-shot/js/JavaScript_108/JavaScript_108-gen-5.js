  let count = 0;
  for (const num of arr) {
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
    if (sum > 0) {
      count++;
    }
    if (isNegative) {
      count++;
    }
  }
  return count;
}
```

These are some examples of problems and their solutions in JavaScript. They cover a range of topics, including array manipulation, string processing, and numerical computations. The problems are designed to be challenging but still accessible to developers with a good understanding of JavaScript.