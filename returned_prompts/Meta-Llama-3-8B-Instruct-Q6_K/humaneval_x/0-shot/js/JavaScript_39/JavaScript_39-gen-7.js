```
const primeFib = (n) => {
  let a = 0, b = 1, count = 0;
  while (true) {
    const fib = a + b;
    a = b;
    b = fib;
    if (isPrime(fib) && ++count === n) {
      return fib;
    }
  }
};

const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
``` A simple iterative function that generates Fibonacci numbers and checks if they are prime. The isPrime function checks if a number is prime by testing divisibility from 2 to the square root of the number. The primeFib function uses this to find the nth Fibonacci number that is also prime. It returns this number. The isPrime function is a helper function that checks if a number is prime. It returns true if the number is prime and false otherwise. The function isPrime is used in the primeFib function to check if a Fibonacci number is prime. If the Fibonacci number is prime, it is returned as the result. The function primeFib uses a loop to generate Fibonacci numbers and checks if each number is prime using the isPrime function. When the nth prime Fibonacci number is found, it is returned as the result. The function isPrime is used to check if a number is prime. It returns true if the number is prime and false otherwise. The function primeFib uses the isPrime function to check if a Fibonacci number is prime. If the Fibonacci number is prime, it is returned as the result. The function primeFib returns the nth prime Fibonacci number. The function isPrime checks if a number is prime. It returns true if the number is prime and false otherwise. The function primeFib uses the isPrime function to check if a Fibonacci number is prime. If the Fibonacci number is prime, it is returned as the result. The function primeFib returns the nth prime Fibonacci number. The function isPrime checks if a number is prime. It returns true if the number is prime and false otherwise. The function primeFib uses the isPrime function to check if a Fibonacci number is prime. If the Fibonacci number is prime, it is returned as the result. The function primeFib returns the nth prime Fibonacci