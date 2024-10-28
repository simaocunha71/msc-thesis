  const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if (num % i === 0) return false;
    return true;
  }

  const fib = (n) => {
    let a = 1, b = 1;
    while (n-- > 0) {
      [a, b] = [b, a + b];
    }
    return a;
  }

  let count = 0, i = 0;
  while (count < n) {
    if (isPrime(fib(i))) count++;
    i++;
  }
  return fib(i-1);
};

console.log(primeFib(1));
console.log(primeFib(2));
console.log(primeFib(3));
console.log(primeFib(4));
console.log(primeFib(5));
```

## Solution

Here we implement a recursive function to check if a number is prime. We also implement a recursive function to generate Fibonacci numbers. The main function `primeFib` uses these two helper functions to generate prime Fibonacci numbers.

`primeFib` uses a while loop to iterate over the Fibonacci numbers. It checks if each Fibonacci number is prime using the `isPrime` function. If it is, it increments a count. The function continues to run until it has found the `n`th prime Fibonacci number.

Finally, it returns the `n`th prime Fibonacci number.

Note: Since the Fibonacci sequence grows very fast, it's not feasible to calculate the nth prime Fibonacci number for large n.

## Discussion

This problem is a good example of how to combine multiple concepts. It involves generating Fibonacci numbers, checking if they are prime, and finding the nth prime Fibonacci number.

This solution is efficient because it uses a while loop to iterate over the Fibonacci numbers, and it uses a simple