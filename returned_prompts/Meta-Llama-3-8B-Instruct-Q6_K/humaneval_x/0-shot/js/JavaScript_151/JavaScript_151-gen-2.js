```
function doubleTheDifference(lst) {
  let sum = 0;
  for (let num of lst) {
    if (typeof num === 'number' && num >= 0 && parseInt(num) === num) {
      if (num % 2 !== 0) {
        sum += Math.pow(num, 2);
      }
    }
  }
  return sum;
}
```


Explanation:
The function `doubleTheDifference` takes a list of numbers as an argument. It initializes a variable `sum` to 0, which will be used to store the sum of squares of odd numbers in the list.

The function then loops through each number in the list using a for-of loop. For each number, it checks if the number is a positive integer using the following conditions:
- `typeof num === 'number'`: checks if the number is a number
- `num >= 0`: checks if the number is positive
- `parseInt(num) === num`: checks if the number is an integer

If the number passes these conditions, the function checks if the number is odd using the modulo operator (`num % 2 !== 0`). If the number is odd, it adds the square of the number to the sum using `Math.pow(num, 2)`.

Finally, the function returns the sum.

This function handles edge cases such as an empty list, negative numbers, and non-integer numbers by ignoring them or treating them as 0. For example, if the input list is `[-1, -2, 0]`, the function will ignore the negative numbers and treat 0 as 0, resulting in a sum of 0. If the input list is `[9, -2]`, the function will ignore the negative number and add the square of 9 to the sum, resulting in a sum of 81. If the input list is `[0]`, the function will treat 0 as 0 and return 0. If the input list is an empty list, the function will return 0.