```java
const factorize = (n) => {
  if (n < 2) return [];
  const primes = [];
  for (let i = 2; i <= n; i++) {
    while (n % i === 0) {
      primes.push(i);
      n /= i;
    }
  }
  return primes;
}
```
