To solve this problem, you can create a helper function that checks if the first and last digits of a number are odd. Then, you can use this helper function in the `specialFilter` function to filter out the numbers that meet the criteria.

Here's how you can do it:

```javascript
const specialFilter = (nums) => {
  // Helper function to check if the first and last digits of a number are odd
  const hasOddFirstAndLastDigits = (num) => {
    const strNum = Math.abs(num).toString();
    const firstDigit = parseInt(strNum[0]);
    const lastDigit = parseInt(strNum[strNum.length - 1]);
    return firstDigit % 2 === 1 && lastDigit % 2 === 1;
  };

  // Filter out numbers that are greater than 10 and have odd first and last digits
  const filteredNums = nums.filter(num => num > 10 && hasOddFirstAndLastDigits(num));

  // Return the length of the filtered array
  return filteredNums.length;
};

// Test cases
console.log(specialFilter([15, -73, 14, -15])); // Output: 1
console.log(specialFilter([33, -2, -3, 45, 21, 109])); // Output: 2
```

In this solution, the `hasOddFirstAndLastDigits` function converts the number to a string, and then extracts the first and last digits using `parseInt`. It then checks if both digits are odd using the modulo operator (`%`). 

The `specialFilter` function uses the `filter` method to create a new array that only includes numbers greater than 10 and with odd first and last digits. It then returns the length of this filtered array.