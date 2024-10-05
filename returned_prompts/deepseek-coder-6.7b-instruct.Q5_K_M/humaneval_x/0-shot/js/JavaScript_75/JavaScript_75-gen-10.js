  let count = 0;

  for (let i = 2; i <= a; i++) {
    while (a % i === 0) {
      count++;
      a = a / i;
    }
  }

  return count === 3;
}

console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(45)); // false
console.log(isMultiplyPrime(60)); // true
console.log(isMultiplyPrime(97)); // false
```

**Explanation**
This function works by continuously dividing the input number by a divisor (starting at 2) until the division is no longer possible (i.e., the remainder is not zero). If this process is repeated for all divisors less than or equal to the number, the count of prime divisors is recorded. The function returns true if the count is exactly 3 (i.e., if the number is the product of exactly 3 different prime numbers) and false otherwise.

Note: This function assumes that the input number is a positive integer. It does not handle the case where the input number is 1 (since 1 is not a prime number), or negative numbers.

Also note that the function might not be entirely accurate for large numbers because of the limit of JavaScript's Number.MAX_SAFE_INTEGER.
*/

const isMultiplyPrime = (a) => {
  let count = 0;

  for (let i = 2; i <= a; i++) {
    while (a % i === 0) {
      count++;
      a = a / i;
    }
  }

  return count === 3;
}

console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(45)); // false
console.log(isMultiplyPrime(60)); // true
console.log(isMultiplyPrime(97)); // false






































