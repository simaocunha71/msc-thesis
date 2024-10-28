Here is the solution to the problem:
```
function skjkasdkd(lst) {
  function isPrime(n) {
    if (n <= 1) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  }

  let maxPrime = 0;
  let sum = 0;

  for (let num of lst) {
    if (isPrime(num) && num > maxPrime) {
      maxPrime = num;
    }
  }

  while (maxPrime > 0) {
    sum += maxPrime % 10;
    maxPrime = Math.floor(maxPrime / 10);
  }

  return sum;
}
```
Here's an explanation of the code:

1. The `isPrime` function checks whether a number is prime or not.
2. The main function `skjkasdkd` iterates through the input list `lst` and finds the largest prime number.
3. It then calculates the sum of the digits of the largest prime number by repeatedly dividing the number by 10 and adding the remainder to the sum until the number becomes 0.
4. The function returns the sum of the digits.

You can test this function with the provided examples to see that it produces the correct output.