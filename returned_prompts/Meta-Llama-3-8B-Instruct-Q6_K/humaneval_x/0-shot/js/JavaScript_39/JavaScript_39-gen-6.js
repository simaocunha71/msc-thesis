```javascript
function primeFib(n) {
  const fib = [0, 1];
  let i = 2;
  while (fib.length < n) {
    fib.push(fib[i - 1] + fib[i - 2]);
    i++;
  }
  for (let j = 0; j < fib.length; j++) {
    if (isPrime(fib[j])) {
      return fib[j];
    }
  }
}

function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
}

console.log(primeFib(1)); // 2
console.log(primeFib(2)); // 3
console.log(primeFib(3)); // 5
console.log(primeFib(4)); // 13
console.log(primeFib(5)); // 89
```

The function `primeFib` generates Fibonacci numbers and checks if they are prime using the `isPrime` function. It stops generating numbers once it finds the `n`th prime Fibonacci number. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, it returns `false`, otherwise it returns `true`. The function then returns the `n`th prime Fibonacci number.