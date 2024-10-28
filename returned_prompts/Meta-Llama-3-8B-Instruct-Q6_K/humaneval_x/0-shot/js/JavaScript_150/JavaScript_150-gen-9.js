Here is a simple JavaScript function that fulfills the requirements:

```javascript
const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const xOrY = (n, x, y) => {
  if (isPrime(n)) {
    return x;
  } else {
    return y;
  }
};
```

In this code, the `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking for divisibility. The `xOrY` function then uses this `isPrime` function to determine whether `n` is prime or not. If it is prime, it returns `x`; otherwise, it returns `y`. 

You can test this function with the examples you provided:

```javascript
console.log(xOrY(7, 34, 12)); // Output: 34
console.log(xOrY(15, 8, 5)); // Output: 5
```  */  