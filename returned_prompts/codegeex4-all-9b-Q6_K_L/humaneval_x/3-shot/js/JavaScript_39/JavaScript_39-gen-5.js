  let fib = [1, 1];
  let prime = [2, 3];
  let fibIndex = 2;
  let primeIndex = 2;

  while (fibIndex <= n) {
    let nextFib = fib[fibIndex - 1] + fib[fibIndex - 2];
    fib.push(nextFib);
    fibIndex++;

    let nextPrime = prime[primeIndex - 1] + prime[primeIndex - 2];
    prime.push(nextPrime);
    primeIndex++;
  }

  let primeFib = prime[n];
  while (!isPrime(primeFib)) {
    primeFib = primeFib + fib[n];
  }

  return primeFib;
}

const isPrime = (number) => {
  if (number < 2) {
    return false;
  }

  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
}