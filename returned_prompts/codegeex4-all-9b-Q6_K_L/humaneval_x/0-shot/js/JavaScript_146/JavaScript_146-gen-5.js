```javascript
const specialFilter = (nums) => {
  // Initialize a counter to keep track of the number of elements that satisfy the condition
  let count = 0;

  // Iterate over each number in the array
  for (let num of nums) {
    // Check if the number is greater than 10
    if (num > 10) {
      // Extract the first and last digits of the number
      const firstDigit = Math.abs(num).toString()[0];
      const lastDigit = Math.abs(num).toString().slice(-1);

      // Check if both digits are odd
      if (firstDigit % 2 === 1 && lastDigit % 2 === 1) {
        // Increment the counter if both conditions are met
        count++;
      }
    }
  }

  // Return the final count
  return count;
};
```

Explanation:
1. Initialize a counter `count` to keep track of the number of elements that satisfy the condition.
2. Iterate over each number in the input array `nums`.
3. For each number, check if it is greater than 10.
4. If the number is greater than 10, extract the first and last digits of the number.
5. Check if both digits are odd.
6. If both digits are odd, increment the counter `count`.
7. Return the final count after iterating over all numbers.