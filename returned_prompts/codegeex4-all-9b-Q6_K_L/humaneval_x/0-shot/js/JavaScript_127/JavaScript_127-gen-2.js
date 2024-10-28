```java
const intersection = (interval1, interval2) => {
  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);
  let length = end - start + 1;

  if (length < 1) {
    return "NO";
  }

  const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  return isPrime(length) ? "YES" : "NO";
}
```
