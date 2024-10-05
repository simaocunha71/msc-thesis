To solve this problem, we can use the concept of modular arithmetic. Modular arithmetic is a type of arithmetic in which numbers "wrap around" when they reach a certain value. In this case, we are working with modulo p, which means that any number that exceeds p will be reduced to its remainder when divided by p.

We can use the following formula to calculate 2^n modulo p:

(base ^ exponent) % modulus

In our case, the base is 2, the exponent is n, and the modulus is p. 

Here's a step-by-step breakdown of the solution:

1. Initialize the result to 1. This will be our final answer.
2. While n is greater than 0, perform the following steps:
   a. Multiply the result by 2.
   b. Subtract 1 from n.
3. Return the result.

The code provided implements this algorithm:

```javascript
const modp = (n, p) => {
  let result = 1;

  while (n > 0) {
    result = (result * 2) % p;
    n--;
  }

  return result;
};
```

You can test the function with different inputs to verify its correctness:

```javascript
console.log(modp(3, 5));  // Output: 3
console.log(modp(1101, 101));  // Output: 2
console.log(modp(0, 101));  // Output: 1
console.log(modp(3, 11));  // Output: 8
console.log(modp(100, 101));  // Output: 1
```

The function `modp` takes two parameters: `n` and `p`. It initializes the `result` variable to 1, which will store the final answer. 

The `while` loop is used to repeatedly multiply the `result` by 2 and subtract 1 from `n` until `n` becomes 0. 

Inside the loop, the `result` is updated by multiplying it by 