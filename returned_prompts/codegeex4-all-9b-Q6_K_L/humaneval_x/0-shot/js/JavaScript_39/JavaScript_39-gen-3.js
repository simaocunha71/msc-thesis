```java
const primeFib = (n) => {
  const isPrime = (num) => {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  let fib = [0, 1];
  let count = 0;
  let i = 2;

  while (count < n) {
    fib[i] = fib[i - 1] + fib[i - 2];
    if (isPrime(fib[i])) count++;
    i++;
  }

  return fib[i - 1];
}
```
