```java
const factorize = (n) => {
  const isPrime = (num) => {
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return num > 1;
  };

  let factors = [];
  for (let i = 2; i <= n; i++) {
    while (isPrime(i) && n % i === 0) {
      factors.push(i);
      n /= i;
    }
  }
  return factors;
}
```
