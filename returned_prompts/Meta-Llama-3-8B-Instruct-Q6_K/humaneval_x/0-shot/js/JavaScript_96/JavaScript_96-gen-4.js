Here is a simple and efficient solution in JavaScript:
```javascript
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
Here's an explanation of the code:

* The `countUpTo` function takes an integer `n` as input and returns an array of prime numbers less than `n`.
* It first checks if `n` is less than or equal to 1, and if so, returns an empty array.
* It then initializes an empty array `primes` to store the prime numbers.
* It loops through the numbers from 2 to `n-1` using a for loop.
* For each number `i`, it checks if it is prime using the `isPrime` function.
* If `i` is prime, it adds it to the `primes` array.
* Finally, it returns the `primes` array.

The `isPrime` function checks if a number `num` is prime by iterating from 2 to the square root of `num` and checking if `num` is divisible by any of these numbers. If it is, it returns `false`, indicating that `num` is not prime. If it reaches the end of the loop without finding a divisor, it returns `true`, indicating that `num` is prime.

This solution has a time complexity of O(n log n) due to the nested loop in the `isPrime` function, but it is still efficient for small to medium-sized inputs. For larger inputs, a more efficient algorithm may be needed.