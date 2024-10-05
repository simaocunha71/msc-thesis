```java
const factorize = (n) => {
  let factors = [];
  let i = 2;
  while (i <= n) {
    if (n % i == 0) {
      factors.push(i);
      n = n / i;
    } else {
      i++;
    }
  }
  return factors;
}
```
