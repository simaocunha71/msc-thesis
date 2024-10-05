```js
const isPrime = (x) => {
  if (x < 2) return false;
  for (let i = 2; i <= Math.sqrt(x); i++) {
    if (x % i === 0) return false;
  }
  return true;
}

const fib = (n) => {
  if (n === 0) return 0;
  if (n === 1) return 1;
  return fib(n - 1) + fib(n - 2);
}

let count = 0;
let i = 0;
while (count < n) {
  if (isPrime(fib(i))) {
    count++;
  }
  i++;
}

return fib(i - 1);
}
```
