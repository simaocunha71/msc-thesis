  let prime_factors = [];
  let factor = 2;
  while (a > 1) {
    if (a % factor == 0) {
      prime_factors.push(factor);
      a = a / factor;
    } else {
      factor += 1;
    }
  }
  return prime_factors.length == 3;
}
// You can also use sieve of Eratosthenes to find prime numbers
// but for simplicity, this solution is fine for this problem.