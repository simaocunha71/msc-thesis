
  const fib = [0, 1];
  let i = 2;
  while (fib.length < n) {
    fib[i] = fib[i - 1] + fib[i - 2];
    if (prime(fib[i])) {
      if (fib[i] === 2) {
        return 2;
      } else if (fib[i] === 3) {
        return 3;
      } else {
        return fib[i];
      }
    }
    i++;
  }
  return -1;
};

const prime = (n) => {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return n > 1;
};

console.log(primeFib(1)); // 2
console.log(primeFib(2)); // 3
console.log(primeFib(3)); // 5
console.log(primeFib(4)); // 13
console.log(primeFib(5)); // 89
















































































































































































































































