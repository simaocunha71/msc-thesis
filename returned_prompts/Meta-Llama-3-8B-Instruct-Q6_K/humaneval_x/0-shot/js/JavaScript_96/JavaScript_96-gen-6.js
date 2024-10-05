Here is the solution to the problem. This function uses a helper function `isPrime` to check if a number is prime, and then generates an array of prime numbers up to `n`.

```javascript
const countUpTo = (n) => {
  const result = [];
  let i = 2;
  while (i < n) {
    if (isPrime(i)) {
      result.push(i);
    }
    i++;
  }
  return result;
};

const isPrime = (num) => {
  if (num < 2) {
    return false;
  }
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
};
```

You can test the function with the examples you provided:

```javascript
console.log(countUpTo(5)); // [2, 3]
console.log(countUpTo(11)); // [2, 3, 5, 7]
console.log(countUpTo(0)); // []
console.log(countUpTo(20)); // [2, 3, 5, 7, 11, 13, 17, 19]
console.log(countUpTo(1)); // []
console.log(countUpTo(18)); // [2, 3, 5, 7, 11, 13, 17]
```