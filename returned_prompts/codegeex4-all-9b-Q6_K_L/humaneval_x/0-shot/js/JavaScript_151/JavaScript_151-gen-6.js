You can solve this problem using the `reduce` method in JavaScript. Here is the solution:

```javascript
const doubleTheDifference = (lst) => {
  // Filter out non-integer and negative numbers
  let filteredList = lst.filter(num => Number.isInteger(num) && num > 0);
  // Calculate the sum of squares of the remaining numbers
  let sumOfSquares = filteredList.reduce((acc, num) => acc + Math.pow(num, 2), 0);
  // Return the doubled result
  return 2 * sumOfSquares;
}
```
In this solution, we first filter out non-integer and negative numbers from the input list. Then we calculate the sum of squares of the remaining numbers using the `reduce` method. Finally, we return the doubled result.