  // Converting strings to fractions
  const [xNum, xDen] = x.split('/').map(Number);
  const [nNum, nDen] = n.split('/').map(Number);

  // Checking if x * n is a whole number
  return (xNum * nNum) % (xDen * nDen) === 0;
}

console.log(simplify("1/5", "5/1")); // true
console.log(simplify("1/6", "2/1")); // false
console.log(simplify("7/10", "10/2")); // false

*/

const simplify = (x, n) => {
  const [xNum, xDen] = x.split("/").map(Number);
  const [nNum, nDen] = n.split("/").map(Number);

  return (xNum * nNum) % (xDen * nDen) === 0;
};

console.log(simplify("1/5", "5/1")); // true
console.log(simplify("1/6", "2/1")); // false
console.log(simplify("7/10", "10/2")); // false
```

This is a simple JavaScript function that takes in two strings representing fractions, splits them into numerators and denominators, and then checks if multiplying the numerators together results in an integer when divided by the product of the denominators.

The function uses the modulus operator (`%`) to check if the remainder is 0, which means that `xNum * nNum` is a multiple of `xDen * nDen`, which in turn means that `x * n` evaluates to a whole number. If that's the case, it returns `true`; otherwise, it returns `false`.

This function assumes that the input strings are valid fractions (i.e., they follow the format `<numerator>/<denominator>`) and that the denominator is not 0.

In the provided examples, the function correctly returns `true` when `x * n` evaluates to a whole number, and `false` otherwise.

- The first example: `1