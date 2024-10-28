To solve this problem, you can follow these steps:

1. Define a function called `sumSquares` that takes a list (`lst`) as an input.
2. Use the `map` method to iterate over the `lst` and round each element to the upper integer (`Ceiling`) using the `Math.ceil()` function. Assign the result to a variable called `roundedLst`.
3. Use the `reduce` method to calculate the sum of squared numbers in the `roundedLst` by multiplying each element by itself and summing up the results. Assign the result to a variable called `sum`.
4. Return the `sum` as the final result.

Here's the code for the solution:

```javascript
const sumSquares = (lst) => {
  const roundedLst = lst.map(Math.ceil);
  const sum = roundedLst.reduce((acc, val) => acc + val * val, 0);
  return sum;
};
```

You can now use the `sumSquares` function to calculate the sum of squared numbers in a given list.

*/

/*You are given a list of numbers.
  You need to return the sum of squared numbers in the given list,
  round each element in the list to the upper int(Ceiling) first.
  Examples:
  For lst = [1,2,3] the output should be 14
  For lst = [1,4,9] the output should be 98
  For lst = [1,3,5,7] the output should be 84
  For lst = [1.4,4.2,0] the output should be 29
  For lst = [-2.4,1,1] the output should be 6
  */
const sumSquares = (lst) => {

const roundedLst = lst.map(Math.ceil);
const sum = roundedLst.reduce((acc, val) => acc + val * val, 0);
return sum;
};

// Example usage:
console.log(sumSquares([1, 2, 3])); // Output: 1