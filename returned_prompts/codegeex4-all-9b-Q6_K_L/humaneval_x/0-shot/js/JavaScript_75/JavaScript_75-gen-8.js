Here is a possible solution in JavaScript:

```javascript
function isPrime(n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 === 0 || n % 3 === 0) return false;
  let i = 5;
  while (i * i <= n) {
    if (n % i === 0 || n % (i + 2) === 0) return false;
    i += 6;
  }
  return true;
}

function isMultiplyPrime(a) {
  if (a <= 1) return false;

  let count = 0;
  for (let i = 2; i <= Math.sqrt(a); i++) {
    while (a % i === 0) {
      a /= i;
      if (isPrime(i)) count++;
    }
  }
  if (a > 1 && isPrime(a)) count++;

  return count >= 3;
}

console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(14)); // false
```

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if it is divisible by any number in that range. The `isMultiplyPrime` function uses this function to check if a number is the multiplication of 3 prime numbers by dividing it by each number from 2 to the square root of the number and counting the number of prime factors. If the count is greater than or equal to 3, it returns true, otherwise, it returns false.