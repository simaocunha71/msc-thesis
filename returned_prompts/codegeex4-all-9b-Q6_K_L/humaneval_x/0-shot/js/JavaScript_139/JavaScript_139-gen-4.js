```js
const specialFactorial = (n) => {
  let result = 1;
  for (let i = n; i >= 1; i--) {
    result *= factorial(i);
  }
  return result;
}

const factorial = (n) => {
  if (n === 0) return 1;
  return n * factorial(n - 1);
}
```
The specialFactorial function takes an integer as input and calculates the Brazilian factorial of this integer. It does this by iterating from n to 1, and for each number, it calculates its factorial and multiplies it with the previous result. The factorial function is a helper function that calculates the factorial of a given number using recursion.