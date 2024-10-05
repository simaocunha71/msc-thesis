Here is a solution in JavaScript:
```javascript
const intersection = (interval1, interval2) => {
  const [start1, end1] = interval1;
  const [start2, end2] = interval2;

  // Check if the intervals intersect
  if (end1 < start2 || end2 < start1) {
    return "NO";
  }

  // Calculate the intersection
  const start = Math.max(start1, start2);
  const end = Math.min(end1, end2);

  // Check if the length of the intersection is a prime number
  const length = end - start + 1;
  let isPrime = true;
  for (let i = 2, sqrt = Math.sqrt(length); i <= sqrt; i++) {
    if (length % i === 0) {
      isPrime = false;
      break;
    }
  }
  return isPrime ? "YES" : "NO";
};
```
The solution first checks if the two intervals intersect by comparing their start and end points. If they do not intersect, it returns "NO". If they do intersect, it calculates the start and end points of the intersection and then checks if the length of the intersection is a prime number. It does this by iterating from 2 to the square root of the length and checking if the length is divisible by any of these numbers. If it is, it sets `isPrime` to `false`. Finally, it returns "YES" if `isPrime` is `true`, and "NO" otherwise.