```js
const removeDuplicates = (numbers) => {
  // Initialize an empty array to store the unique numbers
  let uniqueNumbers = [];

  // Iterate through the input array
  for (let i = 0; i < numbers.length; i++) {
    // Check if the current number is already in the uniqueNumbers array
    if (!uniqueNumbers.includes(numbers[i])) {
      // If not, add it to the uniqueNumbers array
      uniqueNumbers.push(numbers[i]);
    }
  }

  // Return the array of unique numbers
  return uniqueNumbers;
};
```

