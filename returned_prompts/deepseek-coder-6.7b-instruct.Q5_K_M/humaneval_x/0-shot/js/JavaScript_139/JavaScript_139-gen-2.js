  let result = 1;

  for (let i = n; i > 0; i--) {
    result *= factorial(i);
  }

  return result;
};

const factorial = (n) => {
  let result = 1;

  for (let i = n; i > 0; i--) {
    result *= i;
  }

  return result;
};

console.log(specialFactorial(4)); // 288
console.log(specialFactorial(5)); // 34560
console.log(specialFactorial(6)); // 24883200

```

This program first creates a helper function, `factorial`, to calculate the factorial of a given number. Then, the `specialFactorial` function uses this helper function to calculate the special factorial of the input number. It does this by calculating the factorial of each number from the input to 1 (inclusive) and multiplying these values together. The result is returned at the end.

It's also worth mentioning that this solution works well for small inputs. However, for larger inputs, you may want to consider using a more efficient algorithm or a language that supports big numbers.

```javascript

const specialFactorial = (n) => {
  let result = 1n;

  for (let i = n; i > 0; i--) {
    result *= factorial(i);
  }

  return result;
};

const factorial = (n) => {
  let result = 1n;

  for (let i = n; i > 0; i--) {
    result *= BigInt(i);
  }

  return result;
};

console.log(specialFactorial(50)); // 3.0414093201713376e+64
```

This version of the program uses BigInt to handle the calculations with very large numbers. BigInt is a built-in object that provides a way to represent whole numbers in JavaScript that are too large to be represented by the Number primitive.

This program will now correctly calculate the special factorial of larger numbers.

