```java
const isEqualToSumEven = (n) => {
  if (n < 8) {
    return false;
  }
  for (let i = 2; i <= n; i += 2) {
    if (n - i >= 0 && (n - i) % 2 === 0) {
      for (let j = i + 2; j <= n - i; j += 2) {
        if (n - i - j >= 0 && (n - i - j) % 2 === 0) {
          for (let k = j + 2; k <= n - i - j; k += 2) {
            if (n - i - j - k >= 0 && (n - i - j - k) % 2 === 0) {
              return true;
            }
          }
        }
      }
    }
  }
  return false;
}
```
