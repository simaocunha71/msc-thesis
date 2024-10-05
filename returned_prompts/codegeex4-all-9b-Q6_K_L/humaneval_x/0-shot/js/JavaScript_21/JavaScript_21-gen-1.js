The function rescaleToUnit takes an array of numbers as input and returns a new array where the minimum value becomes 0 and the maximum value becomes 1. This is achieved by subtracting the minimum value from each element and then dividing each element by the range of the numbers (maximum - minimum). Here's the implementation of the rescaleToUnit function:

```javascript
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const range = max - min;
  return numbers.map(num => (num - min) / range);
};
```

This function first finds the minimum and maximum values in the input array using the Math.min and Math.max functions. Then, it calculates the range by subtracting the minimum value from the maximum value. Finally, it uses the Array.map function to transform each element in the input array by subtracting the minimum value and dividing by the range. The resulting array is returned as the output of the function.

For example, if we call rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0]), it will return [0.0, 0.25, 0.5, 0.75, 1.0] as expected.