You can solve this problem by using the `filter` method in JavaScript. `filter` method creates a new array with all elements that pass the test implemented by the provided function. In this case, the test is to check if the number is greater than 10 and both first and last digits of a number are odd.

Here is the solution:

```javascript
const specialFilter = (nums) => {
  return nums.filter(num => num > 10 && num.toString().startsWith('1') && num.toString().endsWith('1')).length;
}
```

In this code:

- `num > 10` checks if the number is greater than 10.
- `num.toString().startsWith('1')` checks if the first digit of the number is odd.
- `num.toString().endsWith('1')` checks if the last digit of the number is odd.
- `filter` method returns a new array with all elements that pass the test. `length` returns the length of this new array.

So, the function `specialFilter` returns the length of the array that contains all numbers that are greater than 10 and both first and last digits of a number are odd.