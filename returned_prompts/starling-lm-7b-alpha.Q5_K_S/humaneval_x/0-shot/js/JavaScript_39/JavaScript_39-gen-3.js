  let fib = [2, 3];
  let primes = [2];
  let i = 3;
  while (fib.length < n) {
    fib.push(fib[i - 2] + fib[i - 1]);
    if (isPrime(fib[i])) {
      primes.push(fib[i]);
    }
    i++;
  }
  return primes[n - 1];

};

function isPrime(n) {
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false;
  }
  return true;
}

module.exports = primeFib;





/*
  primeFib returns n-th number that is a Fibonacci number and it's also prime.
  >>> primeFib(1)
  2
  >>> primeFib(2)
  3
  >>> primeFib(3)
  5
  >>> primeFib(4)
  13
  >>> primeFib(5)
  89
*/
const primeFib = (n) => {

Here, the primeFib function takes an input 'n' and returns the n-th number that is a Fibonacci number and also a prime number. 

To solve this problem, the function uses two helper arrays: 'fib' and 'primes'. The 'fib' array stores the Fibonacci sequence, starting with the first two Fibonacci numbers (2 and 3). The 'primes' array stores the prime Fibonacci numbers. 

The function initializes a variable 'i' to 3, as the first two Fibonacci numbers are already in the 'fib' array. It then enters a while loop that continues until the 'fib' array has 'n' elements.

Inside the while loop, the function calculates the next Fibonacci number by adding the last two Fibonacci numbers in the 'fib' array. It then checks if the new Fibonacci number is prime using the 'isPrime' function. If it is prime, the function adds it to the