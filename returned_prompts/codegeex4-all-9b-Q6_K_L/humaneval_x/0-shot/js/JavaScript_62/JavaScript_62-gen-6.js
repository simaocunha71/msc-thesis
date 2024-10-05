To calculate the derivative of a polynomial represented by an array `xs`, you need to apply the power rule of differentiation. The power rule states that the derivative of `x^n` is `n * x^(n-1)`. Using this rule, the derivative of the polynomial `xs[0] + xs[1] * x + xs[2] * x^2 + ....` will be `xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 + ....`. Here's a JavaScript function that calculates the derivative of a polynomial represented by an array `xs`:

```js
const derivative = (xs) => {
    return xs.map((x, i) => x * i);
};
```

The function `derivative` takes an array `xs` as input and returns a new array that represents the derivative of the polynomial. The function uses the `map` method to iterate over each element of the input array `xs`. For each element, the function calculates the derivative using the power rule and returns a new array containing the derivatives. 

The `map` method is a powerful array method in JavaScript that allows you to transform each element of an array and return a new array. In this case, the `map` method is used to calculate the derivative of each element of the input array `xs` and return a new array containing the derivatives.