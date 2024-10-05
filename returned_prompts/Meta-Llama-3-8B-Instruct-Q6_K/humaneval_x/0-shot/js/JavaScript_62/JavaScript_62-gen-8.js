```
const derivative = (xs) => {
  return xs.slice(1).map((x, i) => x * (i + 1));
};
```

Explanation:
The derivative of a polynomial is calculated by multiplying each coefficient with its corresponding power and adding 1 to the power. The function `slice(1)` is used to start the iteration from the second element of the array (index 1) since the first element is the constant term and it does not have a power. The `map` method is used to apply the multiplication operation to each element in the array. The `i + 1` is used to calculate the power of each term. The result is an array of coefficients representing the derivative of the original polynomial.