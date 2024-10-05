```java
const xOrY = (n, x, y) => {
  let is_prime = true;
  if (n < 2) is_prime = false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      is_prime = false;
      break;
    }
  }
  if (is_prime) return x;
  else return y;
}
```
