The main goal of this challenge is to return the sum of squares of the numbers in the list that are odd. Ignore numbers that are negative or not integers. Here is a step-by-step guide to achieve this:

1. Initialize a variable to store the result. Let's call it 'result'.
2. Iterate through the array using a for loop. For each number:

    a. Check if the number is odd and it is an integer. If both conditions are true, add the square of the number to the result. Here is how to determine if a number is odd:
        - If the number modulo 2 is 1, then the number is odd.
        - If the number modulo 2 is 0, then the number is even.
        Here is how to determine if a number is an integer:
        - If the number modulo 1 is 0, then the number is an integer.
        - If the number modulo 1 is not 0, then the number is a float.
3. After the loop, return the result.

Here is the code to achieve this:

```javascript
const doubleTheDifference = (lst) => {
  let result = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] % 2 === 1 && lst[i] % 1 === 0) {
      result += lst[i] ** 2;
    }
  }
  return result;
};
```

This function will return the sum of squares of the odd integers in the list.

For example, if you call `doubleTheDifference([1, 3, 2, 0])`, it will return `1 + 9 + 0 + 0 = 10`.

If you call `doubleTheDifference([-1, -2, 0])`, it will return `0` because all the numbers are either negative or not integers.

If you call `doubleTheDifference([9, -2])`, it will return `81` because 9 is an odd integer and its square is 81.

If you call `doubleTheDifference([0])`, it will return `0`