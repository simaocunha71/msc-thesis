const fib = [0, 1];
let i = 2;
while (fib.length < n) {
  fib.push(fib[i - 1] + fib[i - 2]);
  i++;
}

const primes = [2];
while (fib[fib.length - 1] !== 1) {
  if (isPrime(fib[fib.length - 1])) {
    primes.push(fib[fib.length - 1]);
  }
  fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
}

return primes[primes.length - 1];

};

function isPrime(n) {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}

console.log(primeFib(1));
console.log(primeFib(2));
console.log(primeFib(3));
console.log(primeFib(4));
console.log(primeFib(5));





































































































































































































































