Here is a JavaScript function that solves the problem:
```
const countUpTo = (n) => {
  if (n <= 1) return [];

  const primes = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }
  return primes;
};

const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```
Here's an explanation of how the code works:

1. The `countUpTo` function takes an integer `n` as input and returns an array of prime numbers less than `n`.
2. If `n` is less than or equal to 1, the function returns an empty array.
3. The function uses a `for` loop to iterate from 2 to `n-1`.
4. For each number `i` in the loop, the function calls the `isPrime` function to check if it is prime.
5. If `i` is prime, it is added to the `primes` array.
6. The `isPrime` function takes an integer `num` as input and returns a boolean indicating whether it is prime.
7. The `isPrime` function first checks if `num` is less than or equal to 1, in which case it is not prime.
8. Otherwise, it iterates from 2 to the square root of `num` and checks if `num` is divisible by any of the numbers in the range. If it is, it is not prime.
9. If `num` is not divisible by any of the numbers in the range, it is prime.

You can test the function with different inputs to see that it returns the correct results. For example:
```
console.log(countUpTo(5)); // [2, 3]
console.log(countUpTo(11)); // [2, 3, 5, 7]
console.log(countUpTo(0)); // []
console.log(countUpTo(20)); // [2, 3, 5, 7, 11, 13, 17, 19]
console.log(countUpTo(1)); // []
console.log(countUpTo(18)); // [2, 