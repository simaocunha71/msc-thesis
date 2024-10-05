    let divisor = 2;
    while (n % divisor !== 0) {
      divisor++;
    }
    while (n % (divisor + 1) === 0) {
      divisor++;
    }
    return divisor;
};

/*
Return all primes less than or equal to n. Assume n >= 1.
  >>> findPrimesBelow(10)
  [2, 3, 5, 7]
  >>> findPrimesBelow(100)
  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
  */
const findPrimesBelow = (n) => {
  let sieve = Array(n + 1).fill(true);
  let primes = [];
  for (let i = 2; i <= n; i++) {
    if (sieve[i]) {
      primes.push(i);
      for (let j = i * i; j <= n; j += i) {
        sieve[j] = false;
      }
    }
  }
  return primes;
};

/*
Return the sum of all primes less than or equal to n. Assume n >= 1.
  >>> sumOfPrimesBelow(10)
  17
  >>> sumOfPrimesBelow(100)
  528
  */
const sumOfPrimesBelow = (n) => {
  let primes = findPrimesBelow(n);
  let sum = 0;
  for (let i = 0; i < primes.length; i++) {
    sum += primes[i];
  }
  return sum;
};

/*
Return all composite numbers less than or equal to n. Assume n >= 2.
  >>> allCompositesBel