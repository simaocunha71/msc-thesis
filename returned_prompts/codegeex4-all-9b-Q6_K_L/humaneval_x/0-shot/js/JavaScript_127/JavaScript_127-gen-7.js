```java
const intersection = (interval1, interval2) => {
  if (interval1[0] > interval2[1] || interval2[0] > interval1[1]) {
    return "NO";
  }

  let intersection = [Math.max(interval1[0], interval2[0]), Math.min(interval1[1], interval2[1])];
  let length = intersection[1] - intersection[0] + 1;

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
