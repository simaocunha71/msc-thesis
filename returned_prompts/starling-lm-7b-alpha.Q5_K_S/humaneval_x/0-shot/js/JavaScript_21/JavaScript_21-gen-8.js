To apply a linear transform to a list of numbers such that the smallest number will become 0 and the largest will become 1, you can follow these steps:

1. Find the minimum and maximum values in the list.
2. Subtract the minimum value from all the values in the list.
3. Divide the result by the difference between the maximum and minimum values.
4. Multiply the result by 1, so that the maximum value becomes 1.

Here's how you can implement this in JavaScript:

```javascript
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const range = max - min;

  return numbers.map(number => {
    return ((number - min) / range) * (1);
  });
};
```

This function `rescaleToUnit` takes an array of numbers as an argument. It first finds the minimum and maximum values in the array using the `Math.min` and `Math.max` functions, respectively. Then it calculates the range, which is the difference between the maximum and minimum values.

Next, it uses the `map` function to iterate over each number in the array. For each number, it subtracts the minimum value and divides the result by the range. Finally, it multiplies the result by 1 to ensure that the maximum value becomes 1.

For example, if you call `rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])`, it will return `[0.0, 0.25, 0.5, 0.75, 1.0]`, where the smallest number (1.0) becomes 0 and the largest number (5.0) becomes 1.

You can test the function with different inputs to see how it works.

Note: This solution uses the spread operator (`...`) to pass the numbers as arguments to the `Math.min` and `Math.max` functions, which allows you to find the minimum and maximum values in the array without using additional variables.

Also, the `map` function is used to create a new array with the transformed