Here is the solution:
```javascript
const countNums = (arr) => {
  return arr.reduce((acc, num) => {
    const sumOfDigits = Array.from(String(Math.abs(num))).reduce((a, b) => a + parseInt(b), 0);
    if (sumOfDigits > 0) {
      acc++;
    }
    return acc;
  }, 0);
};
```


Explanation:
The function `countNums` takes an array `arr` as an input. It uses the `reduce` method to iterate over the array. For each number in the array, it calculates the sum of its digits (ignoring the sign) using `Math.abs` to get the absolute value of the number. It then converts the number to a string, splits it into individual digits, and reduces the sum using `reduce`. If the sum of digits is greater than 0, it increments the accumulator `acc`. Finally, it returns the accumulator, which represents the count of numbers with a sum of digits greater than 0.