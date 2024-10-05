To solve this problem we need to find the minimum and maximum values in the array and then scale the array so that the minimum becomes 0 and the maximum becomes 1. Here's a step-by-step explanation:

1. Find the minimum and maximum values in the array using the Math.min() and Math.max() functions respectively.

2. Calculate the scale factor by subtracting the minimum value from the maximum value.

3. Iterate through the array and scale each element using the scale factor. To do this, subtract the minimum value from each element and divide the result by the scale factor.

4. Return the scaled array.

Here's the code that implements this solution:

```javascript
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const scaleFactor = max - min;
  return numbers.map(num => (num - min) / scaleFactor);
};
```

This function uses the spread operator (...) to pass the numbers array as individual arguments to Math.min() and Math.max(). This allows us to find the minimum and maximum values in the array.

The scale factor is calculated by subtracting the minimum value from the maximum value. This gives us the range of values in the array (from 0 to 1).

The map() function is used to iterate through each element in the numbers array. For each element, we subtract the minimum value and divide the result by the scale factor. This scales the element to the range of 0 to 1.

Finally, the scaled array is returned.

This solution ensures that the smallest number in the array becomes 0 and the largest number becomes 1, while all other numbers in between are scaled proportionally.

Examples:

```javascript
console.log(rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])); // [0.0, 0.25, 0.5, 0.75, 1.0]
console.log(rescaleToUnit([-1.0, -2.0, -3.0, -4.0,