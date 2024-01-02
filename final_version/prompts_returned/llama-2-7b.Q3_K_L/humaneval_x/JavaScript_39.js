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
  let res = [];
  for (let i = 2; i < n + 1; i++) {
    if (isPrime.call(null, i)) {
      const f = getFib(i);
      if (f === -1 && isPrime[f]) {
        res.push(f);
        continue;
      }
      if (f > 0) {
        for (let j = i + 1; j < n + 1; j++) {
          const f_prime = getFib(j);
          if (f_prime >= f && isPrime[f_prime]) res.push(f);
        }
      }
    }
  }
  return Math.max(...res);
};

function getFib(n) {
  let fib = 0;
  for (let i = 1; i < n + 1; i++) {
    if (fib === -1 && isPrime[i]) break;
    const f_prime = fib + getFib(i);
    if (f_prime >= fib) return f_prime;
  }
  return -1;
}
