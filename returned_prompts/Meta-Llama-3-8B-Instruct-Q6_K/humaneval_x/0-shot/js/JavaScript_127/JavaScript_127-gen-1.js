The function intersection takes two intervals as input and returns "YES" if the length of their intersection is a prime number, and "NO" otherwise.
Here's the solution:
```javascript
const intersection = (interval1, interval2) => {
  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);
  
  if (start > end) return "NO";
  
  let length = end - start + 1;
  
  if (isPrime(length)) return "YES";
  else return "NO";
};

const isPrime = (n) => {
  if (n <= 1) return false;
  if (n === 2) return true;
  if (n % 2 === 0) return false;
  
  let max = Math.sqrt(n);
  for (let i = 3; i <= max; i += 2) {
    if (n % i === 0) return false;
  }
  return true;
};
```
The function intersection first calculates the start and end points of the intersection by finding the maximum of the two start points and the minimum of the two end points. If the start point is greater than the end point, it means the intervals do not intersect, so the function returns "NO".

Then, it calculates the length of the intersection by subtracting the start point from the end point and adding 1.

Finally, it calls the function isPrime to check if the length is a prime number. If it is, the function returns "YES", otherwise it returns "NO".

The function isPrime checks if a number is prime by iterating from 3 to the square root of the number and checking if the number is divisible by any of these values. If it is, the function returns false. If the number is not divisible by any of these values, the function returns true. If the number is less than or equal to 1, the function returns false. If the number is 2, the function returns true. If the number is an even number greater than 2, the function returns false.