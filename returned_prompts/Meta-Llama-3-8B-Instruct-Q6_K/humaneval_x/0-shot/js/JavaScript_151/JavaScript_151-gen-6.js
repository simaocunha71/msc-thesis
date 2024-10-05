Here is the solution to the problem:

```javascript
const doubleTheDifference = (lst) => {
  let sum = 0;
  for (let num of lst) {
    if (typeof num === 'number' && num % 1 === 0 && num >= 0) {
      if (num % 2 !== 0) {
        sum += Math.pow(num, 2);
      }
    }
  }
  return sum;
};
```

This function iterates over the input list `lst`. For each number, it checks if the number is a positive integer. If it is, it checks if the number is odd. If the number is odd, it adds the square of the number to the sum. Finally, it returns the sum.

The function uses the `Math.pow` method to calculate the square of each odd number. This method takes two arguments: the base number and the exponent. In this case, the exponent is always 2, so it can be replaced with `** 2` for a more concise syntax. However, I have kept the `Math.pow` method for clarity and readability.

The function also uses the `typeof` operator to check if each element of the list is a number. This is necessary because the list can contain other types of data, such as strings or objects. The `% 1 === 0` part checks if the number is an integer, and `num >= 0` checks if the number is non-negative. The `if` statement at the beginning of the function checks if the number is a positive integer.

The function returns the sum of the squares of the odd numbers in the list. If the input list is empty, the function returns 0, as specified in the problem statement.