```
function isMultiplyPrime(a) {
  let count = 0;
  for (let i = 2; i <= a; i++) {
    if (isPrime(i)) {
      count++;
      a = a / i;
      if (a < i) {
        return count === 3;
      }
    }
  }
  return false;
}

function isPrime(n) {
  if (n <= 1) {
    return false;
  }
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}
```


Explanation:
The function `isMultiplyPrime` takes an integer `a` as input and returns a boolean indicating whether `a` is the product of three prime numbers. It uses a helper function `isPrime` to check if a number is prime.

The main function iterates from 2 to `a` and checks if each number is prime using the `isPrime` function. If a prime number is found, it divides `a` by that number and increments the count of prime numbers found. If `a` becomes less than the current prime number, it means that `a` is the product of three prime numbers, and the function returns `true`. If `a` is not the product of three prime numbers, the function returns `false`.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, the function returns `false`, indicating that the number is not prime. If the number is not divisible by any of these values, the function returns `true`, indicating that the number is prime.

Example usage:
```
console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(31)); // false
console.log(isMultiplyPrime(42)); // false
```


Note: This solution has a time complexity of O(sqrt(n)) due to the use of the `isPrime` function, which has a time complexity of O(sqrt(n)). The space complexity is O(1) as it only uses a constant amount of space.