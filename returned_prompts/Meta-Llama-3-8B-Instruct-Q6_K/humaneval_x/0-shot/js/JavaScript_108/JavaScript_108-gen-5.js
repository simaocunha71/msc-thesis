Here is a JavaScript solution for the problem:

```javascript
const countNums = (arr) => {
  return arr.filter(num => {
    const sum = Array.from(String(Math.abs(num))).reduce((a, b) => parseInt(a) + parseInt(b), 0);
    return sum > 0;
  }).length;
};
```

Explanation:
The function `countNums` takes an array of integers as input and returns the count of numbers that have a sum of digits greater than 0.

 Inside the function, we use the `filter` method to create a new array with numbers that have a sum of digits greater than 0.

 We use `Math.abs(num)` to remove the negative sign from the number, and then convert the number to a string using `String()`. This allows us to iterate over each digit of the number.

 We use `Array.from()` to convert the string into an array of digits, and then use the `reduce` method to calculate the sum of the digits. The `reduce` method takes an initial value (0 in this case), and applies a function to each element of the array, returning the accumulated value.

 Finally, we use the `length` property to count the number of elements in the new array, which represents the count of numbers that have a sum of digits greater than 0.

 The function returns this count.