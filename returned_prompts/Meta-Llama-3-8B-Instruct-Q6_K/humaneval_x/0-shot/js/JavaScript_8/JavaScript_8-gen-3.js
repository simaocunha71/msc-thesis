```javascript
const sumProduct = (numbers) => {
  if (numbers.length === 0) {
    return [0, 1];
  }
  const sum = numbers.reduce((acc, current) => acc + current, 0);
  const product = numbers.reduce((acc, current) => acc * current, 1);
  return [sum, product];
};
```


The function `sumProduct` takes a list of integers as an argument. If the list is empty, it returns a tuple containing 0 as the sum and 1 as the product. If the list is not empty, it uses the `reduce` method to calculate the sum and product of all the integers in the list. The `reduce` method applies a function to each element in the list and returns the accumulated result. The initial value of the accumulator is set to 0 for the sum and 1 for the product. The function returns a tuple containing the sum and product.