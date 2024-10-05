  var fibs = [0, 1];
  var primes = [2];
  var index = 2;
  var prime_fibs = [2];

  while (prime_fibs.length < n) {
    let next_fib = fibs[index] + fibs[index-1];
    fibs.push(next_fib);
    if (isPrime(next_fib)) {
      prime_fibs.push(next_fib);
    }
    index += 1;
  }

  return prime_fibs[n-1];
}

const isPrime = (num) => {
  for (let i = 2; i < num; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}