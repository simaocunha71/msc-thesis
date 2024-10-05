Here is a JavaScript solution for the problem:

```javascript
const countNums = (arr) => {
  return arr.reduce((count, num) => {
    if (Math.sign(num) === 1) {
      let sum = 0;
      for (let digit of String(Math.abs(num)).split("")) {
        sum += parseInt(digit);
      }
      if (sum > 0) {
        count++;
      }
    }
    return count;
  }, 0);
};
```

This function works by iterating over each number in the array. If the number is positive, it calculates the sum of its digits (ignoring the sign), and if the sum is greater than 0, it increments the count. The function returns the final count. The initial count is set to 0.

The `Math.sign()` function is used to check if a number is positive or negative. The `String()` function is used to convert the number to a string, and the `split("")` method is used to split the string into individual digits. The `parseInt()` function is used to convert each digit back to an integer, and the sum is calculated by adding up these integers. If the sum is greater than 0, the count is incremented. The final count is returned at the end of the function.