Here is the solution to the problem:

```javascript
const intersection = (interval1, interval2) => {
  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  if (start > end) {
    return "NO";
  }

  let length = end - start + 1;
  let isPrime = true;

  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) {
      isPrime = false;
      break;
    }
  }

  return isPrime ? "YES" : "NO";
};
```

This function first calculates the start and end points of the intersection by taking the maximum of the start points and the minimum of the end points. If the start point is greater than the end point, it means the intervals do not intersect, so the function returns "NO".

Then, it calculates the length of the intersection by subtracting the start point from the end point and adding 1 (since the end point is inclusive).

Finally, it checks if the length is a prime number by iterating from 2 to the square root of the length and checking if the length is divisible by any of these numbers. If it is, the length is not a prime number, so the function returns "NO". Otherwise, it returns "YES".