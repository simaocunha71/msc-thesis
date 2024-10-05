```javascript
const specialFilter = (nums) => {
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    let num = Math.abs(nums[i]);
    if (num > 10 && num % 2 !== 0) {
      let firstDigit = Math.floor(num / Math.pow(10, Math.floor(Math.log10(num))));
      let lastDigit = num % 10;
      if (firstDigit % 2 !== 0 && lastDigit % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
};
```

Explanation:
1. Initialize a count variable to 0.
2. Iterate through the input array of numbers.
3. For each number, calculate its absolute value.
4. If the absolute value of the number is greater than 10 and the number is odd, proceed to the next steps.
5. Extract the first digit of the number by dividing the number by 10 raised to the power of the number of digits in the number.
6. Extract the last digit of the number by taking the remainder of the number divided by 10.
7. If both the first and last digits of the number are odd, increment the count variable.
8. After iterating through all the numbers, return the count variable.