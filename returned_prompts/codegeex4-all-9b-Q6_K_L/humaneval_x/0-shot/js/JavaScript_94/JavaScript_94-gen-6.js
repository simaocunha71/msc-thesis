You can use the `reduce` method to iterate over the list and find the largest prime number. Then, you can use the `reduce` method again to sum the digits of the largest prime number. Here's an example implementation:

```javascript
const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const sumDigits = (num) => {
  return num.toString().split('').reduce((acc, digit) => acc + parseInt(digit), 0);
};

const skjkasdkd = (lst) => {
  const largestPrime = lst.reduce((max, val) => val > max && isPrime(val) ? val : max, 0);
  return sumDigits(largestPrime);
};

// Test cases
console.log(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])); // 10
console.log(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1])); // 25
console.log(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3])); // 13
console.log(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6])); // 11
console.log(skjkasdkd([0,81,12,3,1,21])); // 3
console.log(skjkasdkd([0,8,1,2,1,7])); // 7
```

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if it's divisible by any number in that range.

The `sumDigits` function converts a number to a string, splits it into an array of digits, and then uses the `reduce` method to sum the digits