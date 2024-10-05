let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  return numbers.map(n => (n - min) / (max - min));
};

console.log(rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0]));

```


## ✍️ Answer
```javascript
// function to rescale the array values to 0-1 range
const rescaleToUnit = (numbers) => {
  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  return numbers.map(n => (n - min) / (max - min));
};

console.log(rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])); // [0.0, 0.25, 0.5, 0.75, 1.0]
```

## Explanation
This function works by first determining the smallest and largest values in the input array using the `Math.min()` and `Math.max()` functions.

Then, it uses the `map()` function to create a new array where each element is the result of subtracting the smallest number from the corresponding element in the original array, then dividing the result by the range of the original array (computed as the maximum minus the minimum).

This transformation rescales the numbers in the array to fall within the range 0-1, with the smallest number becoming 0 and the largest number becoming 1.

The result is printed to the console using `console.log()`.

In JavaScript, `...` operator is the spread operator, it allows an iterable to be expanded in places where zero or more arguments or elements are expected.

In the case of `Math.min(...numbers)` and `Math.max(...numbers)`, it's used to get the minimum and maximum values from the array.

The `map()` function in JavaScript creates a new array populated with the results of calling a provided function on every element in the calling array.

In the case of `