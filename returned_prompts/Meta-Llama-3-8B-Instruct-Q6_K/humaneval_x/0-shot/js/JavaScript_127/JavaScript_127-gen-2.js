Here is a JavaScript solution for the problem:

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
    if (n === 2) return true;
    if (n % 2 === 0) return false;

    for (let i = 3; i * i <= n; i += 2) {
      if (n % i === 0) return false;
    }
    return true;
  };

  return isPrime(length) ? "YES" : "NO";
};
```
In this code, we first calculate the start and end points of the intersection interval. If the start is greater than the end, it means the intervals do not intersect, so we return "NO". Otherwise, we calculate the length of the intersection interval. We then define a helper function `isPrime` to check whether a number is prime. Finally, we return "YES" if the length of the intersection interval is prime, otherwise we return "NO". 

For example, when calling `intersection((1, 2), (2, 3))`, the function returns "NO" because the length of the intersection interval (2, 3) is 1, which is not a prime number. When calling `intersection((-3, -1), (-5, 5))`, the function returns "YES" because the length of the intersection interval (-3, -1) is 3, which is a prime number. 

This function assumes that the input intervals are valid, i.e., the start is less than or equal to the end. If the input intervals may be invalid, additional error checking should be added. 

This solution has a time complexity of O(1) because it only performs a constant number of operations. The space complexity is O(1) because it only uses a constant amount of space.  */ 