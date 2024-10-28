```
const countNums = (arr) => {
  return arr.reduce((count, num) => {
    const sumOfDigits = Array.from(String(Math.abs(num))).reduce((acc, digit) => acc + parseInt(digit), 0);
    if (sumOfDigits > 0) {
      count++;
    }
    return count;
  }, 0);
};
```
Explanation:
The function `countNums` takes an array of integers as an argument. It uses the `reduce` method to iterate over the array. For each number, it calculates the sum of its digits using `Array.from` to convert the number to an array of strings, `reduce` to sum up the digits, and `Math.abs` to ignore the sign of the number. It then checks if the sum of digits is greater than 0, and if so, increments a counter. Finally, it returns the count. If the array is empty, the initial value of the count is 0, so the function correctly returns 0 in this case.