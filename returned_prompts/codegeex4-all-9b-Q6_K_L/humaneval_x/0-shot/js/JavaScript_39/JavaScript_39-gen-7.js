```java
const primeFib = (n) => {
  const isPrime = (num) => {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  let fib1 = 0;
  let fib2 = 1;
  let count = 0;
  let result = 0;

  while (count < n) {
    let nextFib = fib1 + fib2;
    fib1 = fib2;
    fib2 = nextFib;

    if (isPrime(nextFib)) {
      count++;
      result = nextFib;
    }
  }

  return result;
}
```