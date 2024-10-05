  // calculate intersection start and end
  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  // if start > end, no intersection
  if (start > end) {
    return "NO";
  }

  // calculate intersection length
  let length = end - start + 1;

  // check if length is prime
  if (length < 2) {
    return "NO";
  }
  for (let i = 2, sqrt = Math.sqrt(length); i <= sqrt; i++) {
    if (length % i === 0) {
      return "NO";
    }
  }
  return "YES";
}

// TEST CASES:
console.log(intersection((1, 2), (2, 3))); //  "NO"
console.log(intersection((-1, 1), (0, 4))); //  "NO"
console.log(intersection((-3, -1), (-5, 5))); //  "YES"



//This is a solution in JavaScript. The key point is to calculate the intersection of two intervals first and then check if the length of the intersection is a prime number. If the length is less than 2, it's not a prime number. If the length is divisible by any number from 2 to the square root of the length, it's not a prime number. Otherwise, it's a prime number.

```





```





```





```





```





```





```





```





```





```





```





```





```





```





```





```





```





```





```





```





```





```





```
