Here is a JavaScript solution for the problem:

```javascript
const specialFilter = (nums) => {
  let count = 0;
  for (let num of nums) {
    if (num > 10) {
      let firstDigit = Math.floor(Math.abs(num) / 10);
      let lastDigit = Math.abs(num) % 10;
      if (firstDigit % 2 !== 0 && lastDigit % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
};
```

The function `specialFilter` iterates over each number in the input array. If the number is greater than 10, it checks if both the first and last digits of the number are odd. If they are, it increments the count. Finally, it returns the count. 

The `Math.floor(Math.abs(num) / 10)` expression calculates the first digit of the number, and the `Math.abs(num) % 10` expression calculates the last digit. The `Math.abs` function is used to ensure that the digits are calculated correctly for negative numbers. The `%` operator is used to get the remainder of the division, which is the last digit of the number. 

The `if (firstDigit % 2 !== 0 && lastDigit % 2 !== 0)` condition checks if both the first and last digits are odd by checking if the remainder of the division of each digit by 2 is not 0. 

This solution has a time complexity of O(n), where n is the number of elements in the input array, because it needs to iterate over each element in the array once. The space complexity is O(1), because it only uses a constant amount of space to store the count and the digits of the numbers. 