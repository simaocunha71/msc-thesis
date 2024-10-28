```javascript
const addElements = (arr, k) => {
  // Create a variable to store the sum
  let sum = 0;
  // Loop over the first k elements of the array
  for (let i = 0; i < k; i++) {
    // If the element has at most two digits, add it to the sum
    if (arr[i] < 100) {
      sum += arr[i];
    }
  }
  // Return the sum
  return sum;
};
```