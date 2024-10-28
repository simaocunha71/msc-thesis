  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  
  return numbers.map(n => (n - min) / (max - min));
};

console.log(rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0]));

// Explanation:
// The function rescaleToUnit takes a list of numbers as its argument.
// It first calculates the minimum and maximum of the list using Math.min and Math.max and their spread operator (...).
// Then it maps over the numbers list, transforming each number by subtracting the minimum and dividing by the range (max - min).
// This rescales the numbers to the range [0, 1].
// Finally, it returns the transformed list.
// The console log outputs the rescaled list [0.0, 0.25, 0.5, 0.75, 1.0].
// This rescaling operation ensures that all numbers in the list are in the range [0, 1], and the smallest number becomes 0 and the largest becomes 1.
```

### Task 5

```javascript
