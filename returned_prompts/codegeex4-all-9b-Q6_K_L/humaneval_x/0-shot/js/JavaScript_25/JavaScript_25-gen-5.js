```java
const factorize = (n) => {
  const is_prime = (num) => {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  let factors = [];
  for (let i = 2; i <= n; i++) {
    while (is_prime(i) && n % i === 0) {
      factors.push(i);
      n /= i;
    }
  }
  return factors;
}
```
