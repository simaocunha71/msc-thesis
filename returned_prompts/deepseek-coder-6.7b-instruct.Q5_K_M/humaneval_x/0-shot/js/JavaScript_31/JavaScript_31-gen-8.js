  if(n < 2) return false;
  for(let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)
    if(n % i === 0) return false;
  return true;
}

//  TEST CASES
console.log(isPrime(6) === false);
console.log(isPrime(101) === true);
console.log(isPrime(11) === true);
console.log(isPrime(13441) === true);
console.log(isPrime(61) === true);
console.log(isPrime(4) === false);
console.log(isPrime(1) === false);

```
This function checks divisibility starting from 2 up to the square root of the number, which is an efficient way to check for primality. If any number is found to be a divisor, the function immediately returns false, indicating that the number is not prime. If no divisors are found by the time the loop has completed, the function returns true, indicating that the number is prime.

The reason we only need to check up to the square root of the number is that a larger factor of the number would be a multiple of a smaller factor that has already been checked.

The reason we start from 2 is because 1 is not a prime number.
```

```javascript
// SOLUTION 2
