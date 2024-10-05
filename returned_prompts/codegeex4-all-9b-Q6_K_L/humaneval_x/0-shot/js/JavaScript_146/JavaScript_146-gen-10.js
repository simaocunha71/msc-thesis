```javascript
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 10 && nums[i] % 2 !== 0) {
      let firstDigit = Math.abs(nums[i]) % 10;
      let lastDigit = Math.floor(Math.abs(nums[i]) / 10) % 10;
      if (firstDigit % 2 !== 0 && lastDigit % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
};
```
This solution iterates through the array of numbers, checking if each number is greater than 10 and has both first and last digits that are odd. If both conditions are met, the count is incremented. Finally, the function returns the count.