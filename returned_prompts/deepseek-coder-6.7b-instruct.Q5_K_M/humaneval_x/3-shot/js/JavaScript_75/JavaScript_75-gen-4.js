  const primeChecker = (n) => {
    if (n < 2) {
      return false;
    }
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  }
  let factors = 0;
  for (let i = 2; i <= a / 2; i++) {
    if (a % i === 0 && primeChecker(i)) {
      factors++;
    }
  }
  return factors === 3;
}
```






[Export of Github issue for [extcode/extcode](https://github.com/extcode/extcode). Generated on 18.03.2023 15:21:18.]
