Here is a simple solution in JavaScript:
```javascript
const intersection = (interval1, interval2) => {
  const start = Math.max(interval1[0], interval2[0]);
  const end = Math.min(interval1[1], interval2[1]);

  if (start > end) {
    return "NO";
  }

  const length = end - start + 1;
  const isPrime = (n) => {
    if (n <= 1) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  };

  return isPrime(length) ? "YES" : "NO";
};
```
The solution works as follows:
1. It calculates the start and end points of the intersection by taking the maximum of the start points and the minimum of the end points of the two intervals.
2. If the start point is greater than the end point, it means the intervals do not intersect, so it returns "NO".
3. It calculates the length of the intersection by subtracting the start point from the end point and adding 1.
4. It checks if the length is a prime number using a helper function `isPrime`.
5. If the length is a prime number, it returns "YES", otherwise it returns "NO".