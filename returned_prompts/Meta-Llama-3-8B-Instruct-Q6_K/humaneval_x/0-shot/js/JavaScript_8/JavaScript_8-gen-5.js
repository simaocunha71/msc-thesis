Here is the solution to the problem:

```javascript
const sumProduct = (numbers) => {
  if (numbers.length === 0) {
    return [0, 1];
  }
  let sum = 0;
  let product = 1;
  for (let number of numbers) {
    sum += number;
    product *= number;
  }
  return [sum, product];
};
```

This function takes an array of numbers as an input. If the array is empty, it returns a tuple with 0 as the sum and 1 as the product. If the array is not empty, it initializes two variables, sum and product, to 0 and 1 respectively. Then it iterates over the array, adding each number to the sum and multiplying each number to the product. Finally, it returns a tuple with the sum and the product.