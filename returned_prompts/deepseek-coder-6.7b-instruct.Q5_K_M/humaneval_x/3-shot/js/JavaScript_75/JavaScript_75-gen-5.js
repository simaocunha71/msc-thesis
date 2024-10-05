  const getPrimes = (n) => {
    const sieve = Array(n).fill(true);
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (sieve[i]) {
        for (let j = i * i; j < n; j += i) {
          sieve[j] = false;
        }
      }
    }
    return Object.entries(sieve).reduce((acc, [index, value], _, { length }) => value ? [...acc, Number(index)] : acc, []);
  }

  const primes = getPrimes(a);
  for (let i = 0; i < primes.length; i++) {
    for (let j = 0; j < primes.length; j++) {
      for (let k = 0; k < primes.length; k++) {
        if (i !== j && j !== k && i !== k) {
          if (primes[i] * primes[j] * primes[k] === a) {
            return true;
          }
        }
      }
    }
  }
  return false;
}



