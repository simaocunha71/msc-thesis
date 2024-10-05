To solve this problem we can use the following steps:

1. Initialize a variable called "sum" to 0. This variable will store the sum of squares of the odd numbers in the list.
2. Iterate through each number in the input list using a for loop.
3. Check if the number is an integer by using the Number.isInteger(number) method. If the number is an integer, check if it is odd by using the (number % 2) % 2 === 1 condition. If the number is odd, calculate the square of the number by using the Math.pow(number, 2) method and add it to the "sum" variable.
4. After iterating through all the numbers in the list, return the value of the "sum" variable.

Here's an example implementation of the solution in JavaScript:

```javascript
const doubleTheDifference = (lst) => {
  let sum = 0;

  for (let i = 0; i < lst.length; i++) {
    if (Number.isInteger(lst[i]) && (lst[i] % 2) % 2 === 1) {
      sum += Math.pow(lst[i], 2);
    }
  }

  return sum;
};
```

You can test this function with the provided test cases:
```javascript
console.log(doubleTheDifference([1, 3, 2, 0]) === 10); // true
console.log(doubleTheDifference([-1, -2, 0]) === 0); // true
console.log(doubleTheDifference([9, -2]) === 81); // true
console.log(doubleTheDifference([0]) === 0); // true
```

This implementation should pass all the test cases and correctly solve the problem.

*/

/* Given a list of numbers, return the sum of squares of the numbers
  in the list that are odd. Ignore numbers that are negative or not integers.
  doubleTheDifference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
  doubleTheDifference([-1, -2, 0