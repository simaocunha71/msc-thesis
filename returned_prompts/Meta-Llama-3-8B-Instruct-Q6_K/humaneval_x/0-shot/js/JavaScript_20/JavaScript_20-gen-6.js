Here is the solution to the problem. This function takes a list of numbers as input and returns the two numbers that are closest to each other.

```javascript
const findClosestElements = (numbers) => {
  // Sort the list of numbers
  numbers.sort((a, b) => a - b);
  
  // Initialize the minimum difference and the closest elements
  let minDiff = Infinity;
  let closestElements = [numbers[0], numbers[0]];
  
  // Iterate over the sorted list of numbers
  for (let i = 0; i < numbers.length - 1; i++) {
    // Calculate the difference between the current and the next number
    let diff = numbers[i + 1] - numbers[i];
    
    // If the difference is smaller than the minimum difference, update the minimum difference and the closest elements
    if (diff < minDiff) {
      minDiff = diff;
      closestElements = [numbers[i], numbers[i + 1]];
    }
  }
  
  // Return the closest elements
  return closestElements;
};
```

This function first sorts the list of numbers in ascending order. Then, it iterates over the sorted list and calculates the difference between the current and the next number. If the difference is smaller than the minimum difference found so far, it updates the minimum difference and the closest elements. Finally, it returns the closest elements. If there are multiple pairs of numbers that are the closest to each other, this function will return the first one it finds.

For example, if you call `findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])`, the function will return `(2.0, 2.2)` because these two numbers are the closest to each other. If you call `findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])`, the function will return `(2.0, 2.0)` because these two numbers are the closest to each other.