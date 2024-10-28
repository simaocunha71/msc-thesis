```javascript
const isMultiplyPrime = (a) => {
  for (let i = 2; i <= a; i++) {
    let isPrime = true;
    for (let j = 2; j * j <= i; j++) {
      if (i % j === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      for (let k = 2; k * k <= a / i; k++) {
        if (a / i % k === 0) {
          let isPrimeK = true;
          for (let l = 2; l * l <= k; l++) {
            if (k % l === 0) {
              isPrimeK = false;
              break;
            }
          }
          if (isPrimeK) {
            for (let m = 2; m * m <= a / (i * k); m++) {
              if (a / (i * k) % m === 0) {
                let isPrimeM = true;
                for (let n = 2; n * n <= m; n++) {
                  if (m % n === 0) {
                    isPrimeM = false;
                    break;
                  }
                }
                if (isPrimeM) {
                  return true;
                }
              }
            }
          }
        }
      }
    }
  }
  return false;
};
```


B:
```javascript
function isMultiplyPrime(a) {
  for (let i = 2; i < 100; i++) {
    for (let j = 2; j < 100; j++) {
      for (let k = 2; k < 100; k++) {
        if (i * j * k === a) {
          if (isPrime(i) && isPrime(j) && isPrime(k)) {
            return true;
          }
        }
      }
    }
  }
  return false;
}

function isPrime(n) {
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}
```
This function uses a nested loop to check all possible combinations of prime numbers that multiply to the given number. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking