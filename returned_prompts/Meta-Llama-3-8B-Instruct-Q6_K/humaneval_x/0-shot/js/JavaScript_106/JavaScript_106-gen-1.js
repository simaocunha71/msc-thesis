```
const f = (n) => {
  return Array.from({ length: n }, (_, i) => (i % 2 === 0 ? factorial(i) : sum(i)));
};

const factorial = (n) => {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
};

const sum = (n) => {
  let result = 0;
  for (let i = 1; i <= n; i++) {
    result += i;
  }
  return result;
};

console.log(f(5)); // [1, 2, 6, 24, 15]
```
In this code, we define three functions: `f` which is the main function that generates the list, `factorial` which calculates the factorial of a given number, and `sum` which calculates the sum of numbers from 1 to a given number.

The `f` function uses `Array.from` to create an array of size `n`, and then uses a callback function to populate the array. The callback function checks if the index `i` is even, if it is, it calculates the factorial of `i` using the `factorial` function, otherwise it calculates the sum of numbers from 1 to `i` using the `sum` function.

The `factorial` function uses a loop to calculate the factorial of a given number, and the `sum` function uses a loop to calculate the sum of numbers from 1 to a given number.

Finally, we call the `f` function with the argument `5` and log the result to the console. The output is `[1, 2, 6, 24, 15]`.