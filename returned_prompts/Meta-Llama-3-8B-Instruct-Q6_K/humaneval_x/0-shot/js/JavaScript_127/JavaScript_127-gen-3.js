Here is the solution in JavaScript:
```
const intersection = (interval1, interval2) => {
  const [start1, end1] = interval1;
  const [start2, end2] = interval2;
  
  const intersectionStart = Math.max(start1, start2);
  const intersectionEnd = Math.min(end1, end2);
  
  if (intersectionStart > intersectionEnd) {
    return "NO";
  }
  
  const intersectionLength = intersectionEnd - intersectionStart + 1;
  
  const isPrime = (n) => {
    if (n <= 1) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  };
  
  return isPrime(intersectionLength) ? "YES" : "NO";
};
```
Explanation:

1. We first calculate the start and end of the intersection by taking the maximum of the start of both intervals and the minimum of the end of both intervals.
2. If the intersection start is greater than the intersection end, it means the intervals don't intersect, so we return "NO".
3. We calculate the length of the intersection by subtracting the intersection start from the intersection end and adding 1 (since the intersection is closed).
4. We define a helper function `isPrime` to check if a number is prime.
5. Finally, we call `isPrime` with the intersection length and return "YES" if it's prime, otherwise "NO".