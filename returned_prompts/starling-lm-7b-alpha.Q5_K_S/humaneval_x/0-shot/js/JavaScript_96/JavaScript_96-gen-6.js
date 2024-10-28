Here's one way you can implement the function:

```javascript
function countUpTo(n) {
  const primes = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }
  return primes;
}

function isPrime(num) {
  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}
```

Explanation:
The `countUpTo` function takes an integer `n` as input and initializes an empty array `primes`. It then uses a `for` loop to iterate from 2 to `n-1`. For each number, it checks if the number is prime using the `isPrime` function. If the number is prime, it is added to the `primes` array using the `push` method. Finally, the function returns the `primes` array.

The `isPrime` function takes a number `num` as input and uses a `for` loop to iterate from 2 to `num-1`. For each number in the loop, it checks if the number evenly divides `num` using the modulus operator (`%`). If the number does evenly divide `num`, the function returns `false`, indicating that `num` is not prime. If no number evenly divides `num`, the function returns `true`, indicating that `num` is prime.

By using these two functions together, the `countUpTo` function can generate an array of the first `n` integers that are prime and less than `n`.

Example usage:

```javascript
console.log(countUpTo(5)); // [2,3]
console.log(countUpTo(11)); // [2,3,5,7]
console.log(countUpTo(0)); // []
console.log(countUpTo(20)); // [2,3,5,7,11,13,17,19]
console.log(countUpTo(1)); // []
console