To solve this problem, we can use a simple approach. We can first sort the input array in ascending order. Then, we can iterate through the array and calculate the difference between each pair of adjacent elements. We will keep track of the pair with the smallest difference. Finally, we will return the pair of numbers with the smallest difference.

Here is the implementation in JavaScript:

```javascript
const findClosestElements = (numbers) => {
  // Sort the input array in ascending order
  numbers.sort((a, b) => a - b);

  // Initialize variables to keep track of the closest pair and their difference
  let closestPair = [numbers[0], numbers[1]];
  let smallestDifference = numbers[1] - numbers[0];

  // Iterate through the array and calculate the difference between each pair of adjacent elements
  for (let i = 1; i < numbers.length - 1; i++) {
    let difference = numbers[i + 1] - numbers[i];
    // If the difference is smaller than the current smallest difference, update the closest pair and smallest difference
    if (difference < smallestDifference) {
      closestPair = [numbers[i], numbers[i + 1]];
      smallestDifference = difference;
    }
  }

  // Return the closest pair of numbers
  return closestPair;
};
```

Let's test the function with the provided examples:

```javascript
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])); // Output: [2.0, 2.2]
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])); // Output: [2.0, 2.0]
```

Both examples return the expected output.