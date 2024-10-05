Here is the solution to the problem:

```javascript
function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
}

const skjkasdkd = (lst) => {
  let maxPrime = 0;
  for (let num of lst) {
    if (isPrime(num) && num > maxPrime) {
      maxPrime = num;
    }
  }
  let sum = 0;
  while (maxPrime > 0) {
    sum += maxPrime % 10;
    maxPrime = Math.floor(maxPrime / 10);
  }
  return sum;
};
```


The function `skjkasdkd` takes a list of integers as an argument. It iterates over the list to find the largest prime number. Then, it calculates the sum of the digits of the largest prime number. The function `isPrime` checks whether a number is prime or not. It does this by checking divisibility from 2 to the square root of the number. If the number is divisible by any of these values, it is not prime. If the number is not divisible by any of these values, it is prime. The function `skjkasdkd` returns the sum of the digits of the largest prime number.