  let fib1 = 1;
  let fib2 = 1;
  let fibNext = fib1 + fib2;
  let primeNumbers = [2];
  let i = 3;
  let count = 2;

  while(count < n) {
    if (isFib(fibNext) && isPrime(fibNext)) {
      count++;
    }
    i++;
    fib1 = fib2;
    fib2 = fibNext;
    fibNext = fib1 + fib2;
  }

  return fibNext;

  function isFib(num) {
    return primeNumbers.includes(num);
  }

  function isPrime(num) {
    for (let j = 2, sqrt = Math.sqrt(num); j <= sqrt; j++)
      if (num % j === 0) return false; 
    primeNumbers.push(num);
    return true;
  }
};

console.log(primeFib(1));
console.log(primeFib(2));
console.log(primeFib(3));
console.log(primeFib(4));
console.log(primeFib(5));




A: You should start from the first Fibonacci number, which is 1. Then you generate the next Fibonacci number by adding the previous two.
Then you check if the generated number is prime by looping from 2 to sqrt(n) and checking if n is divisible by any of these numbers. If n is divisible by any of these numbers, it is not prime. Otherwise, it is prime.
If the number is prime, then you increment your count of prime Fibonacci numbers. When your count reaches n, you return that number.
Here is the corrected code:


const primeFib = (n) => {
  let fib1 = 1;
  let fib2 = 1;
  let fibNext = fib1 + fib2;
  let primeNumbers = [2];
  let i = 3;
  let count = 2;

  while(count < n) {
    if (isFib(fibNext) && is