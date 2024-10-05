  let factor = 2;
  while (factor <= n) {
    if (n % factor === 0) {
      n /= factor;
    } else {
      factor++;
    }
  }
  return factor;
}

console.log(largestPrimeFactor(13195)); // 29
console.log(largestPrimeFactor(2048)); // 2
```

### Problem 4: Find the missing number in a given integer array

