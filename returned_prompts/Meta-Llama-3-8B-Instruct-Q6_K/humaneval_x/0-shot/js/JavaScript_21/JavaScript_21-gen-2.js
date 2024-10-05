```
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map((num) => (num - min) / (max - min));
};
```


Explanation:
*   We first find the minimum and maximum values in the input array using the `Math.min` and `Math.max` functions with the spread operator (`...`) to apply these functions to all elements in the array.
*   Then, we use the `map` method to transform each element in the array. For each element, we calculate the new value by subtracting the minimum value from the original value and then dividing the result by the difference between the maximum and minimum values.
*   This transformation ensures that the smallest number in the input array becomes 0 and the largest becomes 1, effectively rescaling the values to a unit interval. The resulting array is returned by the `rescaleToUnit` function.