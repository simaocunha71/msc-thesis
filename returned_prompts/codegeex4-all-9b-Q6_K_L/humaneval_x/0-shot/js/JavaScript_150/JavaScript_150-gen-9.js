```java
const xOrY = (n, x, y) => {
  let isPrime = true;
  if (n < 2) isPrime = false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      isPrime = false;
      break;
    }
  }
  return isPrime ? x : y;
}
```
