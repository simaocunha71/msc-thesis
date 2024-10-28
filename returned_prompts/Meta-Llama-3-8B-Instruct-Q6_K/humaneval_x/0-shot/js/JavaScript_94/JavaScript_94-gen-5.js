Here is the solution to the problem:

```javascript
function skjkasdkd(lst) {
  function isPrime(n) {
    if (n <= 1) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    let sqrt = Math.sqrt(n);
    for (let i = 3; i <= sqrt; i += 2) {
      if (n % i === 0) return false;
    }
    return true;
  }

  let maxPrime = -1;
  for (let num of lst) {
    if (isPrime(num) && num > maxPrime) {
      maxPrime = num;
    }
  }

  if (maxPrime === -1) {
    return 0;
  }

  let sumOfDigits = 0;
  while (maxPrime > 0) {
    sumOfDigits += maxPrime % 10;
    maxPrime = Math.floor(maxPrime / 10);
  }

  return sumOfDigits;
}
```


Explanation:

1.  We define a helper function `isPrime(n)` that checks if a given number `n` is prime.
2.  We iterate through the input list `lst` and for each number, we check if it is prime using the `isPrime(n)` function. If it is prime and greater than the current maximum prime, we update the maximum prime.
3.  If no prime numbers are found in the list, we return 0.
4.  We calculate the sum of digits of the maximum prime number by repeatedly dividing it by 10 and adding the remainder to the sum.
5.  Finally, we return the sum of digits.