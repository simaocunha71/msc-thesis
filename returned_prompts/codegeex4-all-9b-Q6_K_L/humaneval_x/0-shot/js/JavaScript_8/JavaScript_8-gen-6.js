The `sumProduct` function can be implemented using the `reduce` method in JavaScript. The `reduce` method executes a reducer function on each element of the array, resulting in a single output value.

Here is an example of how you can implement the `sumProduct` function:

```javascript
const sumProduct = (numbers) => {
  const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
  const product = numbers.reduce((accumulator, currentValue) => accumulator * currentValue, 1);
  return [sum, product];
};
```

The `reduce` method takes two arguments: a reducer function and an initial value.

In this case, the reducer function adds each element to the accumulator and multiplies each element to the accumulator respectively. The initial value for the sum is 0 and for the product is 1.

The function then returns an array with the sum and product as its elements.

Here is an example of how you can use the `sumProduct` function:

```javascript
console.log(sumProduct([])); // Output: [0, 1]
console.log(sumProduct([1, 2, 3, 4])); // Output: [10, 24]
```

This should help you solve the problem.