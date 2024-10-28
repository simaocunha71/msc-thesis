Here is a JavaScript solution for the problem:
```javascript
const countUpTo = (n) => {
  const result = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      result.push(i);
    }
  }
  return result;
};

const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```
Here's an explanation of the code:

The `countUpTo` function takes an integer `n` as input and returns an array of prime numbers less than `n`.

The function uses a `for` loop to iterate from 2 to `n-1`. For each number `i` in this range, it checks if the number is prime using the `isPrime` function. If the number is prime, it adds it to the `result` array.

The `isPrime` function takes an integer `num` as input and returns a boolean indicating whether the number is prime.

The `isPrime` function works by checking if the number is less than or equal to 1 (in which case it's not prime), or if it has any divisors other than 1 and itself. It does this by iterating from 2 to the square root of the number, and checking if the number is divisible by any of these values. If it finds a divisor, it returns `false`. If it doesn't find any divisors, it returns `true`.

You can test the `countUpTo` function with different inputs to see the expected output. For example:
```javascript
console.log(countUpTo(5)); // [2, 3]
console.log(countUpTo(11)); // [2, 3, 5, 7]
console.log(countUpTo(0)); // []
console.log(countUpTo(20)); // [2, 3, 5, 7, 11, 13, 17, 19]
console.log(countUpTo(1)); // []
console.log(countUpTo(18)); // [2, 3, 5, 7, 11, 13, 17]
``` 