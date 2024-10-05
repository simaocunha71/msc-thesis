Here is the solution in JavaScript:

```javascript
const intersection = (interval1, interval2) => {
  const [start1, end1] = interval1;
  const [start2, end2] = interval2;
  
  let intersectionStart = Math.max(start1, start2);
  let intersectionEnd = Math.min(end1, end2);
  
  if (intersectionStart > intersectionEnd) {
    return "NO";
  }
  
  const intersectionLength = intersectionEnd - intersectionStart + 1;
  
  if (intersectionLength <= 1) {
    return "NO";
  }
  
  for (let i = 2; i * i <= intersectionLength; i++) {
    if (intersectionLength % i === 0) {
      return "NO";
    }
  }
  
  return "YES";
};
```

This function calculates the intersection of two given intervals, and then checks if the length of the intersection is a prime number. If the length is not prime, or if the intervals do not intersect at all, the function returns "NO". Otherwise, it returns "YES". The function uses the Math.max and Math.min functions to find the start and end of the intersection, and then calculates the length of the intersection. It then checks if the length is prime by iterating from 2 to the square root of the length and checking if the length is divisible by any of these numbers. If it is, the length is not prime, and the function returns "NO". Otherwise, the function returns "YES".