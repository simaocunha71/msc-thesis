```js
const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
};

const fib = (n) => {
  if (n <= 1) return n;
  return fib(n - 1) + fib(n - 2);
};

let count = 0;
let i = 0;
while (count < n) {
  if (isPrime(fib(i))) {
    count++;
  }
  i++;
}

return fib(i - 1);
};
```