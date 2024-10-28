
let limit = Math.sqrt(n) + 1;
for (let i = 2; i < limit; i++) {
  if (n % i === 0) {
    return false;
  }
}
return true;
};

In this code, we're defining a function called `isPrime` that takes in a single argument `n`. The function will return `true` if the number `n` is prime, and `false` otherwise.

To determine if a number is prime, we need to check all numbers up to the square root of the given number. We start the loop at `i = 2` since all prime numbers are greater than 1. We increment `i` by 1 in each iteration until we reach `limit`, which is `Math.sqrt(n) + 1`.

Inside the loop, we check if `n` is divisible by `i` using the modulo operator `%`. If the remainder is 0, then `n` is divisible by `i` and not prime, so we return `false`. If the loop finishes without finding any divisors, we can conclude that `n` is prime, and we return `true`.

This algorithm is efficient because we only need to check up to the square root of the number, rather than all numbers up to the number itself. This is because, if a number has a divisor greater than its square root, it must also have a divisor less than or equal to its square root.

The time complexity of this algorithm is O(sqrt(n)), and the space complexity is O(1).

Overall, this code provides a simple and efficient way to determine if a given number is prime or not.

*/






function isPrime(n) {
  let limit = Math.sqrt(n) + 1;
  for (let i = 2; i < limit; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

console.log(isPrime(6));  // false
console.log(isPrime(101));  // true
console.log(isPrime(11));  // true
console.log(isPr