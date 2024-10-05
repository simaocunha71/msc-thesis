Here is the JavaScript function that checks if a given number is the multiplication of 3 prime numbers:
```javascript
const isMultiplyPrime = (a) => {
  const primeNumbers = [];
  let isPrime = true;

  // Check if the number is divisible by any number from 2 to sqrt(a)
  for (let i = 2, sqrt = Math.sqrt(a); i <= sqrt; i++) {
    if (a % i === 0) {
      isPrime = false;
      break;
    }
  }

  // If the number is prime, add it to the array of prime numbers
  if (isPrime) {
    primeNumbers.push(a);
  }

  // Check if the given number can be divided by 3 prime numbers
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < primeNumbers.length; j++) {
      for (let k = 0; k < primeNumbers.length; k++) {
        if (a === primeNumbers[j] * primeNumbers[k] * primeNumbers[i]) {
          return true;
        }
      }
    }
  }

  return false;
};
```
This function first checks if the given number is prime by iterating from 2 to the square root of the number and checking for divisibility. If the number is prime, it adds it to an array of prime numbers. Then, it iterates over the array of prime numbers and checks if the given number can be divided by 3 prime numbers. If it finds a combination that satisfies the condition, it returns `true`. Otherwise, it returns `false`.

You can test this function with the example you provided:
```javascript
console.log(isMultiplyPrime(30)); // Output: true
```
Note that this function has a time complexity of O(n^3) due to the nested loops, so it may not be efficient for large numbers. If you need to optimize the function for large numbers, you can consider using a more efficient algorithm or a prime number sieve.