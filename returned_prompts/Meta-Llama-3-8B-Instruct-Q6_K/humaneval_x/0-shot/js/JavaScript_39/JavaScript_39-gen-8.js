```
function primeFib(n) {
  let a = 0, b = 1, count = 0;
  while (true) {
    const fib = a + b;
    a = b;
    b = fib;
    if (isPrime(fib)) {
      count++;
      if (count === n) return fib;
    }
  }
}

function isPrime(num) {
  if (num < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
}
```

Explanation:
The function `primeFib` uses a while loop to generate Fibonacci numbers until it finds the `n-th` prime Fibonacci number. The function `isPrime` checks whether a number is prime or not. In the `primeFib` function, we keep track of the count of prime Fibonacci numbers generated. When the count reaches `n`, we return the current Fibonacci number. The `isPrime` function uses a simple trial division method to check whether a number is prime or not. It iterates from 2 to the square root of the number and checks for divisibility. If the number is divisible by any of these values, it is not prime. Otherwise, it is prime.